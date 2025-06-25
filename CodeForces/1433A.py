t = int(input())
for _ in range(t):
    x = input().strip()
    d = int(x[0]) 
    n = len(x)      
    presses = (d - 1) * 10 + (n * (n + 1)) // 2
    print(presses)
