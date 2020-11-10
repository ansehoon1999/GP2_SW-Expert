T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    if c < a :
        result = a - c
    elif a <= c <= b :
        result = 0
    elif c > b :
        result = -1



    print('#', end='')
    print(test_case, result)
