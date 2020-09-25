

T = 10

for test_case in range(1, T+1) :
    count = 0
    test = int(input())
    str1 = input()
    str1_list = list(str1) #검색할 단어
    str2 = input()
    str2_list = list(str2) #검색 대상 문장

    for i in range(len(str2_list)-len(str1_list)) :
        if str2[i:i+len(str1_list)] == str1:
            count = count +1
        else :
            continue
    print('#', end='')
    print(test, count)
        
