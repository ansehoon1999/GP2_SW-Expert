

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    for i in range(N) :
        a, b = map(float, input().split())
        count = count + a * b
        
        
    print('#', end = "")
    print(test_case, count)
