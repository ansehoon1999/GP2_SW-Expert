T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())

    b = input()
    b = list(b)

    result = []
    
    for i in range(len(b)) :
        if b[i] != '+' :
            result.append(int(b[i]))

    print('#', end = "")
          
    print(test_case, sum(result))

    

