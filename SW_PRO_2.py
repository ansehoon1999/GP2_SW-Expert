T = int(input())



def okay(x) :
    lis = []

    while True :
        if x == 0 :
            break
        t = x % 10
        lis.append(t)
        x = x // 10
    
    length1 = len(lis)
    length2 = int(length1/2) + 1
    
    for i in range(length2) :
        if lis[i] == lis[length1-1-i]:
            result = 1
        else :
            result = 0
            break
    return result

for test_case in range(1, T+1) :
    
    count = 0
    a, b = map(int, input().split())
    for i in range(a, b+1) :
        if (i ** (1/2)) % 1 == 0 :
            root = i ** (1/2)
            
            if okay(i) == 1 and okay(root) == 1:

                count = count +1
                
        else :
            continue
    print('#', end='')
    print(test_case, count)
