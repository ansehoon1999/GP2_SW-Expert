T = int(input())

for test_case in range(1, T + 1):
    a = int(input())
    num = []
    count = 0
    
    for i in range(a) :
        b = int(input())
        num.append(b)

    avg = sum(num)/a

    for i in range(len(num)) :
        if num[i] > avg :
            temp = num[i] - avg

        elif num[i] < avg :
            temp = avg - num[i]

        elif num[i] == avg :
            temp = 0

        count = count + temp
            
    
        

    print('#', end='')
    print(test_case, int(count/2))
    
