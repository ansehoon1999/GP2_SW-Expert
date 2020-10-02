T = int(input())

for test_case in range(1, T + 1):

    a, b, c = map(int, input().split())

    
    if a == b and a == c and b == c:
        result = a

    elif a == b and a != c and b != c :
        result = c

    elif a != b and a == c and b != c :
        result = b

    elif a != b and a != c and b == c :
        result = a

    print('#', end ='')
    print(test_case, result)

    
    
