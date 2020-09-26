T = 10
for test_case in range(1, T + 1):
    num = int(input())
    a, b = map(int, input().split())
    cost = 1
    for i in range(b) :
        cost = cost * a

    print('#', end='')
    print(num, cost)
