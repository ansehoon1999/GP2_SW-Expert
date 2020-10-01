T = int(input())


for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    count = 0
    m_str = format(m, 'b')

    lis1 = list(m_str)
    lis1.reverse()

    
    for i in range(len(lis1), 30) :
        lis1.append('0')

    for i in range(n) :
        if lis1[i] == '1' :
            count = count + 1

    if count == n :
        result = 'ON'
    else :
        result = 'OFF'

    print('#', end='')
    print(test_case, result)
