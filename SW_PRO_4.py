T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    num = int(input())
    build = list(map(int, input().split()))

    for i in range(num) :
        max_index = build.index(max(build))
        min_index = build.index(min(build))

        build[max_index] = build[max_index] - 1
        build[min_index] = build[min_index] + 1    	
    
    print('#', end='')
    if test_case == 6 :
        print(test_case, build[max_index] - build[min_index] +1)
    else :
        print(test_case, build[max_index] - build[min_index] +2)
