def is_nearly_lucky(n):
    count = 0
    for digit in str(n):
        if digit == '4' or digit == '7':
            count += 1
    return "YES" if all(c in '47' for c in str(count)) else "NO"

# Input
n = input()
print(is_nearly_lucky(n))