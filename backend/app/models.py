from pydantic import BaseModel, Field


class TranslateRequest(BaseModel):
    """텍스트 → 점자 변환 요청 모델"""
    text: str = Field(..., description="변환할 한글 텍스트", min_length=1)
    use_liblouis: bool = Field(default=False, description="libLouis 사용 여부 (fallback)")


class TranslateResponse(BaseModel):
    """점자 변환 응답 모델"""
    original_text: str = Field(..., description="원본 텍스트")
    braille: str = Field(..., description="점자 결과")
    method: str = Field(..., description="사용된 변환 방법 (rule-based 또는 liblouis)")
    success: bool = Field(..., description="변환 성공 여부")
    error: str | None = Field(None, description="오류 메시지 (있을 경우)")
