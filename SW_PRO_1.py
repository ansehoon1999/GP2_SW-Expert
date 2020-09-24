T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = 0
    num = int(input())
    building = list(map(int, input().split()))
    
    
    for i in range(num) :
        if building[i] == 0 :
            continue
        
        other  = max(building[i-2], building[i-1],building[i+1],building[i+2])
        if(building[i] - other) <= 0 :
            continue
        else :
            count = count + building[i] - other
    print('#', end='')
    print(test_case, count)

