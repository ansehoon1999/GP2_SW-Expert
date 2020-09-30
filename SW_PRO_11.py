T = int(input())

for test_case in range(1, T + 1):
    a= input()
    a_list = list(a)
    a_target = []
    count = 0
    for i in range(len(a_list)) :
        a_target.append('0')


    for i in range(len(a_list)) :
        if a_list[i] == a_target[i] :
            continue
        else :

            if a_list[i] == '1' :
                for j in range(i, len(a_list)) :
                    a_target[j] = '1'
                count = count + 1
                
        
            elif a_list[i] == '0' :
                for j in range(i, len(a_list)) :
                    a_target[j] = '0'
                count = count + 1
    print('#', end='')            
    print(test_case, count)
                
    

        
    
