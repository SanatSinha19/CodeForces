n = int(input())
t = input()

s = ""
i = 1
index = 0

while index < n:
    s += t[index]
    index += i
    i += 1

print(s)
