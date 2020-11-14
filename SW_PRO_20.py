T = int(input())
for test_case in range(1, T + 1):
    string = input()
    
    lis = list(string)
    re_lis = []
    lis_len = len(lis)

    for i in range(lis_len) :

        if lis[i] == 'a' :
            continue

        elif lis[i] == 'e' :
            continue

        elif lis[i] == 'i' :
            continue

        elif lis[i] == 'o' :
            continue

        elif lis[i] =='u' :
            continue

        else :
            re_lis.append(lis[i])


    print('#', end='')
    print(test_case, ''.join(re_lis))
    
    
