T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    lis1 = []
    count = 0 
    for i in range(num) :
        a, b = map(int, input().split())
        lis1.append([a,b])
        
    
    for i in range(num) :
        cenx = lis1[i][0]
        ceny = lis1[i][1]

        for j in range(num) :
            if i == j :
                continue

            if ((cenx < lis1[j][0]) and (ceny < lis1[j][1])) or ((cenx > lis1[j][0]) and (ceny > lis1[j][1])) :
                continue
            else :
                
                count = count+1


    print('#', end='')
    print(test_case, int(count/2))
