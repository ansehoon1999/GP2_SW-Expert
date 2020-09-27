

T = 10
for test_case in range(1, T + 1):
    main = []
    count = 0
    num = int(input())
    
    
    for i in range(8) :
        string = input()
        main.append(list(string))


    for a in range(8) :
        for b in range(9-num) :
            target1 = main[a][b:b+num]
            target2 = []
            for x in main :
                target2.append(x[a])

            target2 = target2[b:b+num]
            
            if target1 == target1[::-1]  :
                count = count + 1
            
                

            if target2 == target2[::-1] :
                count = count + 1
               
    print('#', end='')
    print(test_case, count)
    



                    
        
        
        
