T = int(input())
for test_case in range(1, T + 1):

    a, b, c, d, e = map(int, input().split())

    if a < 40 :
        a = 40
    if b < 40 :
        b = 40
    if c < 40 :
        c = 40
    if d < 40 :
        d = 40
    if e < 40 :
        e = 40

    avg = int((a + b + c + d + e) / 5)

    print('#', end = '')
    print(test_case, avg)
