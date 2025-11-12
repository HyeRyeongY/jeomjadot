"""
약자 규칙 테스트 - '자' 글자 확인
"""

from app.services.advanced_braille_converter import advanced_converter

results = []

# 1. 약자 사용
braille_with = advanced_converter.convert("자", use_contractions=True)
results.append("약자 사용 (use_contractions=True)")
results.append(f"'자' → {braille_with}")
results.append(f"점자 길이: {len(braille_with)}")
results.append("")

# 2. 약자 미사용
braille_without = advanced_converter.convert("자", use_contractions=False)
results.append("약자 미사용 (use_contractions=False)")
results.append(f"'자' → {braille_without}")
results.append(f"점자 길이: {len(braille_without)}")
results.append("")

# 3. 문장에서 테스트
sentence = "점자 변환"
braille_sentence_with = advanced_converter.convert(sentence, use_contractions=True)
braille_sentence_without = advanced_converter.convert(sentence, use_contractions=False)

results.append("문장 테스트: '점자 변환'")
results.append(f"약자 사용: {braille_sentence_with}")
results.append(f"약자 미사용: {braille_sentence_without}")
results.append("")

# 4. 다른 약자들도 테스트
test_chars = ['가', '나', '다', '마', '바', '사', '자', '하']
results.append("1음절 약자 테스트:")
for char in test_chars:
    with_contraction = advanced_converter.convert(char, use_contractions=True)
    without_contraction = advanced_converter.convert(char, use_contractions=False)
    results.append(f"{char}: 약자O={with_contraction} (길이{len(with_contraction)}) / 약자X={without_contraction} (길이{len(without_contraction)})")

# 파일로 저장
output_file = "contraction_test_results.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print(f"테스트 결과가 {output_file}에 저장되었습니다.")

# 간단한 검증
assert len(braille_with) == 1, f"약자 사용 시 '자'의 길이는 1이어야 함 (현재: {len(braille_with)})"
assert len(braille_without) == 2, f"약자 미사용 시 '자'의 길이는 2여야 함 (현재: {len(braille_without)})"
print("✓ 약자 규칙이 올바르게 적용되었습니다!")
