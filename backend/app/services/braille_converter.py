"""
점자 변환 서비스
Rule-based 변환과 libLouis fallback 지원
"""

from typing import Literal
from app.services.korean_braille import text_to_braille


class BrailleConverter:
    """점자 변환기 클래스"""

    def __init__(self):
        self.liblouis_available = False
        try:
            import louis
            self.liblouis_available = True
            self.louis = louis
        except ImportError:
            self.liblouis_available = False

    def convert(
        self,
        text: str,
        use_liblouis: bool = False
    ) -> tuple[str, Literal["rule-based", "liblouis"]]:
        """
        텍스트를 점자로 변환

        Args:
            text: 변환할 텍스트
            use_liblouis: libLouis 사용 여부

        Returns:
            (점자 결과, 사용된 방법) 튜플
        """
        if not text:
            return "", "rule-based"

        # libLouis 사용 요청 및 사용 가능한 경우
        if use_liblouis and self.liblouis_available:
            try:
                braille = self._convert_with_liblouis(text)
                return braille, "liblouis"
            except Exception:
                # libLouis 실패 시 rule-based로 fallback
                pass

        # Rule-based 변환 (기본)
        braille = text_to_braille(text)
        return braille, "rule-based"

    def _convert_with_liblouis(self, text: str) -> str:
        """
        libLouis를 사용한 점자 변환

        Args:
            text: 변환할 텍스트

        Returns:
            점자 문자열

        Raises:
            Exception: libLouis 변환 실패 시
        """
        if not self.liblouis_available:
            raise Exception("libLouis is not available")

        # libLouis 한글 테이블 사용 (ko-g1.ctb 또는 ko-g2.ctb)
        # 주의: libLouis의 한글 지원은 제한적일 수 있음
        try:
            braille = self.louis.translateString(["ko-g1.ctb"], text)
            return braille
        except Exception as e:
            raise Exception(f"libLouis translation failed: {str(e)}")

    def is_liblouis_available(self) -> bool:
        """libLouis 사용 가능 여부 반환"""
        return self.liblouis_available


# 전역 변환기 인스턴스
converter = BrailleConverter()
