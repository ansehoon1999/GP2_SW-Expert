

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    count = 0
    num_list = list(map(int, input().split()))

    
    avg = sum(num_list)/len(num_list)
    for i in range(num) :
        if num_list[i] <= avg :
            count = count + 1
    print('#', end='')
    print(test_case, count)
    
            

    
