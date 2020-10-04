
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())

    second = input() #5 3
    sec_list = list(second.split()) #['2','5', '3']

    lis1 = []
    result = []
    for i in range(1, n+1) :
        lis1.append(str(i)) #['1','2','3','4','5']
        result.append(str(i))
    
    
    for i in range(n) :
        for j in range(k) :
            if lis1[i] == sec_list[j] :
                result.remove(lis1[i])
                
    print('#', end='')
    print(test_case, end=' ')
    for i in range(len(result)) :
        print(result[i], end=' ')
        
    
    print()
