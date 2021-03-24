
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input()

    count_list = []
    original_list = list(a)
    original_list_length = len(original_list)
    tmp = set(original_list)
    after_list = list(tmp)

    count = 0
    
    for i in range(len(after_list)) :
        for j in range(original_list_length) :
            if after_list[i] == original_list[j] :
                count = count + 1

        count_list.append(count)

        count = 0

    x = original_list_length / min(count_list)

    print('#', end='')        
    print(test_case, int(x))
    count_list = []
