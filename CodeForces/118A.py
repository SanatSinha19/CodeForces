def process_string(s):
    vowels = {'a', 'o', 'y', 'e', 'u', 'i'}
    result = ''
    for ch in s:
        ch_lower = ch.lower()
        if ch_lower not in vowels:
            result += '.' + ch_lower
    return result
input_string = input()
print(process_string(input_string))
