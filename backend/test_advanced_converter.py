"""
고급 점자 변환기 테스트
국립국어원 규정 적용 확인
"""

from app.services.advanced_braille_converter import advanced_converter


def test_korean_basic():
    """기본 한글 변환 테스트"""
    print("=" * 60)
    print("1. 기본 한글 변환 테스트")
    print("=" * 60)

    test_cases = [
        "안녕",
        "한글",
        "점자",
        "변환",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print("-" * 40)
    print()


def test_numbers():
    """숫자 표기 테스트"""
    print("=" * 60)
    print("2. 숫자 표기 테스트")
    print("=" * 60)

    test_cases = [
        "123",
        "2024",
        "0",
        "456789",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print(f"설명: 숫자표(⠼) + 각 숫자 점자")
        print("-" * 40)
    print()


def test_english():
    """영문자 표기 테스트"""
    print("=" * 60)
    print("3. 영문자 표기 테스트")
    print("=" * 60)

    test_cases = [
        "Hello",
        "World",
        "ABC",
        "xyz",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print(f"설명: 영어표(⠰) + 대문자표(⠠) + 알파벳 점자")
        print("-" * 40)
    print()


def test_punctuation():
    """문장 부호 테스트"""
    print("=" * 60)
    print("4. 문장 부호 테스트")
    print("=" * 60)

    test_cases = [
        "안녕하세요.",
        "점자, 변환",
        "정말요?",
        "대단해!",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print("-" * 40)
    print()


def test_mixed():
    """혼합 텍스트 테스트"""
    print("=" * 60)
    print("5. 혼합 텍스트 테스트 (한글+숫자+영문+부호)")
    print("=" * 60)

    test_cases = [
        "안녕하세요 123",
        "Hello 세계",
        "2024년 점자 변환기",
        "점자닷 v0.1.0",
        "Tel: 010-1234-5678",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print("-" * 40)
    print()


def test_contractions():
    """약자 규칙 테스트"""
    print("=" * 60)
    print("6. 약자 규칙 테스트")
    print("=" * 60)

    test_cases = [
        ("가", "전부 약자"),
        ("나", "전부 약자"),
        ("것", "전부 약자"),
        ("그래서", "부분 약자"),
        ("그러나", "부분 약자"),
    ]

    for text, description in test_cases:
        braille_with = advanced_converter.convert(text, use_contractions=True)
        braille_without = advanced_converter.convert(text, use_contractions=False)
        print(f"원본: {text} ({description})")
        print(f"약자 적용: {braille_with}")
        print(f"약자 미적용: {braille_without}")
        print("-" * 40)
    print()


def test_real_sentences():
    """실제 문장 테스트"""
    print("=" * 60)
    print("7. 실제 문장 테스트")
    print("=" * 60)

    test_cases = [
        "안녕하세요, 점자닷입니다.",
        "한글을 점자로 변환합니다.",
        "2024년 11월에 만들었어요!",
        "숫자 123과 영어 Hello를 지원합니다.",
    ]

    for text in test_cases:
        braille = advanced_converter.convert(text)
        print(f"원본: {text}")
        print(f"점자: {braille}")
        print(f"길이: 원본 {len(text)}자 → 점자 {len(braille)}자")
        print("-" * 40)
    print()


def run_all_tests():
    """모든 테스트 실행"""
    print("\n[고급 점자 변환기 테스트 시작]\n")

    test_korean_basic()
    test_numbers()
    test_english()
    test_punctuation()
    test_mixed()
    test_contractions()
    test_real_sentences()

    print("[모든 테스트 완료!]\n")


if __name__ == "__main__":
    run_all_tests()
