from pydantic import BaseModel, Field


class TranslateRequest(BaseModel):
    """텍스트 → 점자 변환 요청 모델"""
    text: str = Field(..., description="변환할 한글 텍스트", min_length=1)
    use_liblouis: bool = Field(default=False, description="libLouis 사용 여부 (fallback)")
    use_advanced_rules: bool = Field(
        default=True,
        description="국립국어원 규정 적용 (숫자, 영문, 약자 등). False시 기본 자모 매핑만 사용"
    )
    use_contractions: bool = Field(
        default=True,
        description="약자 사용 여부 (것, 그래서 등). use_advanced_rules=True일 때만 적용"
    )


class TranslateResponse(BaseModel):
    """점자 변환 응답 모델"""
    original_text: str = Field(..., description="원본 텍스트")
    braille: str = Field(..., description="점자 결과")
    method: str = Field(..., description="사용된 변환 방법 (rule-based, advanced, 또는 liblouis)")
    success: bool = Field(..., description="변환 성공 여부")
    error: str | None = Field(None, description="오류 메시지 (있을 경우)")
