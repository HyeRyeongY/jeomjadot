"""
국립국어원 한글 점자 규정을 완전 적용한 고급 변환기
"""

import re
from typing import List, Tuple
from app.services.korean_braille import decompose_hangul, CHOSEONG_BRAILLE, JUNGSEONG_BRAILLE, JONGSEONG_BRAILLE
from app.services.braille_rules import (
    NUMBER_SIGN, NUMBER_BRAILLE,
    ENGLISH_SIGN, UPPER_CASE_SIGN, ENGLISH_LOWER_BRAILLE, ENGLISH_UPPER_BRAILLE,
    PUNCTUATION_BRAILLE,
    FULL_CONTRACTIONS, PARTIAL_CONTRACTIONS
)


class AdvancedBrailleConverter:
    """국립국어원 규정 기반 고급 점자 변환기"""

    def __init__(self):
        self.use_contractions = True  # 약자 사용 여부

    def convert(self, text: str, use_contractions: bool = True) -> str:
        """
        텍스트를 점자로 변환

        Args:
            text: 변환할 텍스트
            use_contractions: 약자 사용 여부

        Returns:
            점자 문자열
        """
        if not text:
            return ""

        self.use_contractions = use_contractions

        # 1. 텍스트를 토큰으로 분리 (한글, 숫자, 영문, 부호)
        tokens = self._tokenize(text)

        # 2. 각 토큰을 점자로 변환
        braille_parts = []
        for token_type, token_value in tokens:
            braille = self._convert_token(token_type, token_value)
            braille_parts.append(braille)

        return "".join(braille_parts)

    def _tokenize(self, text: str) -> List[Tuple[str, str]]:
        """
        텍스트를 토큰으로 분리

        Returns:
            [(token_type, token_value), ...]
            token_type: 'korean', 'number', 'english', 'punctuation', 'space'
        """
        tokens = []
        i = 0

        while i < len(text):
            char = text[i]

            # 공백 및 줄바꿈
            if char in ' \n\t':
                tokens.append(('space', char))
                i += 1

            # 한글
            elif self._is_korean(char):
                # 연속된 한글 모으기
                korean_word = ""
                while i < len(text) and self._is_korean(text[i]):
                    korean_word += text[i]
                    i += 1
                tokens.append(('korean', korean_word))

            # 숫자
            elif char.isdigit():
                # 연속된 숫자 모으기
                number = ""
                while i < len(text) and text[i].isdigit():
                    number += text[i]
                    i += 1
                tokens.append(('number', number))

            # 영문자
            elif char.isalpha():
                # 연속된 영문자 모으기
                english = ""
                while i < len(text) and text[i].isalpha():
                    english += text[i]
                    i += 1
                tokens.append(('english', english))

            # 문장 부호
            else:
                tokens.append(('punctuation', char))
                i += 1

        return tokens

    def _is_korean(self, char: str) -> bool:
        """한글인지 확인"""
        if not char:
            return False
        code = ord(char)
        return 0xAC00 <= code <= 0xD7A3  # 한글 음절 범위

    def _convert_token(self, token_type: str, token_value: str) -> str:
        """토큰을 점자로 변환"""

        if token_type == 'space':
            return token_value

        elif token_type == 'korean':
            return self._convert_korean(token_value)

        elif token_type == 'number':
            return self._convert_number(token_value)

        elif token_type == 'english':
            return self._convert_english(token_value)

        elif token_type == 'punctuation':
            return self._convert_punctuation(token_value)

        return token_value

    def _convert_korean(self, text: str) -> str:
        """한글을 점자로 변환 (약자 규칙 적용)"""

        # 약자 사용 시 전부 약자 확인
        if self.use_contractions and text in FULL_CONTRACTIONS:
            return FULL_CONTRACTIONS[text]

        # 부분 약자 확인 (예: 그래서, 그러나 등)
        if self.use_contractions:
            for contraction, braille in PARTIAL_CONTRACTIONS.items():
                if text == contraction:
                    return braille

        # 일반 변환 (자모 분해)
        result = []
        for char in text:
            braille_char = self._convert_korean_char(char)
            result.append(braille_char)

        return "".join(result)

    def _convert_korean_char(self, char: str) -> str:
        """한글 음절 하나를 점자로 변환"""
        decomposed = decompose_hangul(char)

        if not decomposed:
            return char

        choseong, jungseong, jongseong = decomposed

        braille = ""

        # 초성 추가
        if choseong in CHOSEONG_BRAILLE:
            braille += CHOSEONG_BRAILLE[choseong]

        # 중성 추가
        if jungseong in JUNGSEONG_BRAILLE:
            braille += JUNGSEONG_BRAILLE[jungseong]

        # 종성 추가 (있는 경우)
        if jongseong and jongseong in JONGSEONG_BRAILLE:
            braille += JONGSEONG_BRAILLE[jongseong]

        return braille

    def _convert_number(self, number: str) -> str:
        """
        숫자를 점자로 변환

        규칙: 숫자표(⠼) + 숫자 점자
        예: "123" -> ⠼⠁⠃⠉
        """
        braille = NUMBER_SIGN  # 숫자표

        for digit in number:
            if digit in NUMBER_BRAILLE:
                braille += NUMBER_BRAILLE[digit]
            else:
                braille += digit

        return braille

    def _convert_english(self, text: str) -> str:
        """
        영문자를 점자로 변환

        규칙:
        - 소문자: 영어표(⠰) + 소문자 점자
        - 대문자: 대문자표(⠠) + 소문자 점자
        - 연속된 대문자: 대문자표 + 대문자표 + ...
        """
        braille = ENGLISH_SIGN  # 영어표 (문장 시작에 한 번)

        for char in text:
            if char.isupper():
                # 대문자: 대문자 표시 + 소문자 점자
                braille += UPPER_CASE_SIGN
                braille += ENGLISH_UPPER_BRAILLE.get(char.lower(), char)
            else:
                # 소문자
                braille += ENGLISH_LOWER_BRAILLE.get(char, char)

        return braille

    def _convert_punctuation(self, punct: str) -> str:
        """문장 부호를 점자로 변환"""
        return PUNCTUATION_BRAILLE.get(punct, punct)


# 전역 인스턴스
advanced_converter = AdvancedBrailleConverter()
