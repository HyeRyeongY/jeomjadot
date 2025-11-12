"""
점자 변환 API 라우터
"""

from fastapi import APIRouter, HTTPException
from app.models import TranslateRequest, TranslateResponse
from app.services.braille_converter import converter

router = APIRouter()


@router.post("/translate", response_model=TranslateResponse)
async def translate_to_braille(request: TranslateRequest) -> TranslateResponse:
    """
    한글 텍스트를 점자로 변환하는 엔드포인트

    - **text**: 변환할 한글 텍스트
    - **use_liblouis**: libLouis 사용 여부 (기본값: False)
    - **use_advanced_rules**: 국립국어원 규정 적용 (숫자, 영문, 약자 등) (기본값: True)
    - **use_contractions**: 약자 사용 여부 (기본값: True)

    Returns:
        - **original_text**: 원본 텍스트
        - **braille**: 점자 결과
        - **method**: 사용된 변환 방법 (rule-based, advanced, 또는 liblouis)
        - **success**: 성공 여부
        - **error**: 오류 메시지 (있을 경우)
    """
    try:
        # 입력 텍스트 검증
        if not request.text or not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="변환할 텍스트를 입력해주세요"
            )

        # libLouis 사용 요청 시 사용 가능 여부 확인
        if request.use_liblouis and not converter.is_liblouis_available():
            return TranslateResponse(
                original_text=request.text,
                braille="",
                method="rule-based",
                success=False,
                error="libLouis가 설치되지 않았습니다. rule-based 변환을 사용해주세요."
            )

        # 점자 변환 수행
        braille, method = converter.convert(
            text=request.text,
            use_liblouis=request.use_liblouis,
            use_advanced_rules=request.use_advanced_rules,
            use_contractions=request.use_contractions
        )

        return TranslateResponse(
            original_text=request.text,
            braille=braille,
            method=method,
            success=True,
            error=None
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"점자 변환 중 오류가 발생했습니다: {str(e)}"
        )


@router.get("/translate/health")
async def translate_health():
    """변환 서비스 상태 확인"""
    return {
        "status": "healthy",
        "liblouis_available": converter.is_liblouis_available()
    }
