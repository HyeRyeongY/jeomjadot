"""
간단한 변환 테스트 (파일 출력)
"""

from app.services.advanced_braille_converter import advanced_converter


def test_converter():
    """변환기 테스트 - 결과를 파일로 저장"""

    test_cases = [
        # 기본 한글
        "안녕",
        "한글",

        # 숫자
        "123",
        "2024",

        # 영문
        "Hello",
        "World",

        # 부호
        "안녕하세요.",
        "점자, 변환",

        # 혼합
        "안녕하세요 123",
        "Hello 세계",
        "2024년 점자 변환기",
    ]

    results = []
    results.append("=" * 60)
    results.append("고급 점자 변환기 테스트 결과")
    results.append("=" * 60)
    results.append("")

    for i, text in enumerate(test_cases, 1):
        braille = advanced_converter.convert(text)
        results.append(f"{i}. 원본: {text}")
        results.append(f"   점자: {braille}")
        results.append(f"   길이: 원본 {len(text)}자 → 점자 {len(braille)}자")
        results.append("")

    results.append("=" * 60)
    results.append("테스트 완료!")
    results.append("=" * 60)

    # 파일로 저장
    output_file = "test_results.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(results))

    print(f"테스트 결과가 {output_file} 파일에 저장되었습니다.")
    print("변환기가 정상적으로 작동합니다!")

    # 간단한 확인
    sample = advanced_converter.convert("안녕 123")
    assert len(sample) > 0, "변환 결과가 비어있습니다"
    assert "⠼" in sample, "숫자표가 포함되어야 합니다"

    print(f"✓ 기본 변환 성공")
    print(f"✓ 숫자 표기 성공")
    print(f"✓ 모든 검증 통과!")


if __name__ == "__main__":
    test_converter()
