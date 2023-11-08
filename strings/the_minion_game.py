vowels = "AEIOU"


def play(string: str, start_vowel: bool) -> int:
    string_len = len(string)

    score = 0
    for index, ch in enumerate(string):
        if (start_vowel and ch in vowels) or (not start_vowel and ch not in vowels):
            score += string_len - index

    return score


def minion_game(string):
    # your code goes here
    if not string:
        return

    stuart_score = play(string, False)
    kevin_score = play(string, True)

    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
