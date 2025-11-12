"""
한글 점자 변환 테스트 스크립트
"""

from app.services.korean_braille import text_to_braille, decompose_hangul


def test_decompose():
    """한글 분해 테스트"""
    print("=" * 50)
    print("한글 분해 테스트")
    print("=" * 50)

    test_chars = ['한', '글', '점', '자', '안', '녕']

    for char in test_chars:
        result = decompose_hangul(char)
        if result:
            cho, jung, jong = result
            print(f"{char} -> 초성: {cho}, 중성: {jung}, 종성: {jong}")
        else:
            print(f"{char} -> 분해 실패")

    print()


def test_conversion():
    """점자 변환 테스트"""
    print("=" * 50)
    print("점자 변환 테스트")
    print("=" * 50)

    test_cases = [
        "안녕",
        "감사",
        "점자",
        "한글",
        "변환",
        "안녕하세요",
        "감사합니다",
        "한글 점자 변환기",
        "점자는 시각 장애인을 위한 문자입니다",
    ]

    for text in test_cases:
        braille = text_to_braille(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print(f"길이: 원본 {len(text)}자 -> 점자 {len(braille)}자")
        print("-" * 50)

    print()


def test_special_chars():
    """특수 문자 테스트"""
    print("=" * 50)
    print("특수 문자 테스트")
    print("=" * 50)

    test_cases = [
        "안녕!",
        "점자?",
        "감사.",
        "한글, 점자",
        "숫자: 123",
        "영어: Hello",
    ]

    for text in test_cases:
        braille = text_to_braille(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print("-" * 50)

    print()


if __name__ == "__main__":
    print("\n🔤 한글 점자 변환 테스트 시작\n")

    test_decompose()
    test_conversion()
    test_special_chars()

    print("✅ 모든 테스트 완료\n")
