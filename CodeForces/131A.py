def fix_caps_lock(word):
    if len(word) == 1:
        return word.swapcase()
    if word.isupper() or (word[0].islower() and word[1:].isupper()):
        return word.swapcase()
    return word

word = input().strip()
print(fix_caps_lock(word))
