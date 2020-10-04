
T = int(input())

for test_case in range(1, T + 1):

    n, b, c = map(int, input().split())

    max_cost = min(b,c)
    if n >= b+c :
        min_cost = 0

    else :
        min_cost = (b+c)-n

    print('#', end='')
    print(test_case, max_cost, min_cost)
    
        
    
