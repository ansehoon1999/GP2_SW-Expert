T = int(input())

for test_case in range(1, T + 1):

    string = input()
    lis = list(string)
    lis_len = len(lis)

    for i in range(1, lis_len+1) :
        for a in range(lis_len-i+1) :
            target1 = lis[a:a+i]
            target2 = target1[::-1]

            if target1 == target2 :
                most = target1

            else :
                continue
    print('#', end='')
    print(test_case, len(most))
            
        
