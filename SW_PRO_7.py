T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cost = int(input())
    what = ''
    if cost % 2 == 0 :
        what = 'Even'
    else :
        what = 'Odd'

    print('#', end='')
    print(test_case, what)
