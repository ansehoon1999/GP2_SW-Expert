

T = int(input())
for test_case in range(1, T + 1):
    result = []    
    st = input()
    a = sorted(list(st))

    b = [0 for i in range(len(a))]

    for i in range(len(a)) :
        for j in range(len(a)):
            
            
            if a[i] == a[j] and i != j and b[i] == 0 and b[j] == 0:
                b[i] = 1
                b[j] = 1
    for i in range(len(a)) :
        if b[i] == 0 :
            result.append(a[i])

    if len(result) == 0 :
        print('#', end='')
        print(test_case, 'Good')
    else :
        print('#', end='')
        print(test_case, ''.join(result))
			



			

    

    
    
    
        
