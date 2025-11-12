"""
한글 점자 변환 매핑
한국 점자 규칙: 6점식 점자 사용
유니코드 점자 범위: U+2800 ~ U+28FF
"""

# 초성 (자음) → 점자 매핑
CHOSEONG_BRAILLE = {
    'ㄱ': '⠈',  # U+2808
    'ㄲ': '⠈⠈',
    'ㄴ': '⠉',  # U+2809
    'ㄷ': '⠊',  # U+280A
    'ㄸ': '⠊⠊',
    'ㄹ': '⠐',  # U+2810
    'ㅁ': '⠑',  # U+2811
    'ㅂ': '⠘',  # U+2818
    'ㅃ': '⠘⠘',
    'ㅅ': '⠠',  # U+2820
    'ㅆ': '⠠⠠',
    'ㅇ': '',    # 초성 ㅇ은 점자로 표기하지 않음
    'ㅈ': '⠨',  # U+2828
    'ㅉ': '⠨⠨',
    'ㅊ': '⠰',  # U+2830
    'ㅋ': '⠋',  # U+280B
    'ㅌ': '⠓',  # U+2813
    'ㅍ': '⠙',  # U+2819
    'ㅎ': '⠚',  # U+281A
}

# 중성 (모음) → 점자 매핑
JUNGSEONG_BRAILLE = {
    'ㅏ': '⠣',  # U+2823
    'ㅐ': '⠗',  # U+2817
    'ㅑ': '⠜',  # U+281C
    'ㅒ': '⠜⠗',
    'ㅓ': '⠎',  # U+280E
    'ㅔ': '⠝',  # U+281D
    'ㅕ': '⠱',  # U+2831
    'ㅖ': '⠌',  # U+280C
    'ㅗ': '⠥',  # U+2825
    'ㅘ': '⠧',  # U+2827
    'ㅙ': '⠧⠗',
    'ㅚ': '⠽',  # U+283D
    'ㅛ': '⠬',  # U+282C
    'ㅜ': '⠍',  # U+280D
    'ㅝ': '⠏',  # U+280F
    'ㅞ': '⠏⠗',
    'ㅟ': '⠍⠗',
    'ㅠ': '⠩',  # U+2829
    'ㅡ': '⠪',  # U+282A
    'ㅢ': '⠺',  # U+283A
    'ㅣ': '⠕',  # U+2815
}

# 종성 (받침) → 점자 매핑
JONGSEONG_BRAILLE = {
    'ㄱ': '⠁',  # U+2801
    'ㄲ': '⠁⠁',
    'ㄳ': '⠁⠄',
    'ㄴ': '⠒',  # U+2812
    'ㄵ': '⠒⠅',
    'ㄶ': '⠒⠴',
    'ㄷ': '⠔',  # U+2814
    'ㄹ': '⠂',  # U+2802
    'ㄺ': '⠂⠁',
    'ㄻ': '⠂⠢',
    'ㄼ': '⠂⠃',
    'ㄽ': '⠂⠄',
    'ㄾ': '⠂⠔',
    'ㄿ': '⠂⠃',
    'ㅀ': '⠂⠴',
    'ㅁ': '⠢',  # U+2822
    'ㅂ': '⠃',  # U+2803
    'ㅄ': '⠃⠄',
    'ㅅ': '⠄',  # U+2804
    'ㅆ': '⠄⠄',
    'ㅇ': '⠶',  # U+2836
    'ㅈ': '⠅',  # U+2805
    'ㅊ': '⠆',  # U+2806
    'ㅋ': '⠖',  # U+2816
    'ㅌ': '⠦',  # U+2826
    'ㅍ': '⠲',  # U+2832
    'ㅎ': '⠴',  # U+2834
}

# 한글 자모 분해를 위한 유니코드 값
HANGUL_BASE = 0xAC00
CHOSEONG_BASE = 588
JUNGSEONG_BASE = 28

# 초성 리스트 (19개)
CHOSEONG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트 (21개)
JUNGSEONG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트 (28개, 받침 없음 포함)
JONGSEONG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def decompose_hangul(char: str) -> tuple[str, str, str] | None:
    """
    한글 음절을 초성, 중성, 종성으로 분해

    Args:
        char: 한글 음절 (예: '한')

    Returns:
        (초성, 중성, 종성) 튜플 또는 None (한글이 아닌 경우)
    """
    if not char or len(char) != 1:
        return None

    code = ord(char)

    # 한글 음절 범위 확인 (가-힣)
    if code < HANGUL_BASE or code > HANGUL_BASE + 11171:
        return None

    code -= HANGUL_BASE

    choseong_index = code // CHOSEONG_BASE
    jungseong_index = (code % CHOSEONG_BASE) // JUNGSEONG_BASE
    jongseong_index = code % JUNGSEONG_BASE

    choseong = CHOSEONG_LIST[choseong_index]
    jungseong = JUNGSEONG_LIST[jungseong_index]
    jongseong = JONGSEONG_LIST[jongseong_index]

    return choseong, jungseong, jongseong


def char_to_braille(char: str) -> str:
    """
    한글 음절 하나를 점자로 변환

    Args:
        char: 한글 음절

    Returns:
        점자 문자열
    """
    decomposed = decompose_hangul(char)

    if not decomposed:
        # 한글이 아닌 경우 그대로 반환 (공백, 특수문자 등)
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


def text_to_braille(text: str) -> str:
    """
    한글 텍스트를 점자로 변환

    Args:
        text: 변환할 한글 텍스트

    Returns:
        점자 문자열
    """
    if not text:
        return ""

    result = []

    for char in text:
        braille_char = char_to_braille(char)
        result.append(braille_char)

    return "".join(result)
