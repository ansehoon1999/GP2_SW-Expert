
T = int(input())

for test_case in range(1, T + 1):
    a = input()
    a_list = list(a)
    a_list2 = []
    for i in range(len(a_list)) :
        if a_list[i] == 'b' :
            a_list2.append('d')

        elif a_list[i] == 'd' :
            a_list2.append('b')

        elif a_list[i] == 'p' :
            a_list2.append('q')

        elif a_list[i] == 'q' :
            a_list2.append('p')


    print('#', end='')
    print(test_case, ''.join(a_list2[::-1]))
            
