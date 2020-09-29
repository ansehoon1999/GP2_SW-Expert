T = int(input())

for test_case in range(1, T + 1):
    xmin, ymin, xmax, ymax = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    count = 0

    if x1 == x2 :
        if xmin == x1 :
            print('##1')
            count = 4
        elif xmax == x1 :
            print('##2')
            count = 4
        elif y1 <= ymin <= y2 and y1 <= ymax <= y2 :
            print('##3')
            count=2
        elif y1 <= ymin <= y2 and ((y1 <= ymax <= y2) == False) :
            print('##4')
            count = 1
        elif ((y1 <= ymin <= y2) == False) and y1 <= ymax <= y2 :
            print('##5')
            count = 1
        elif ((y1 <= ymin <= y2) == False) and ((y1 <= ymax <= y2) == False) :
            print('##6')
            count = 0
    elif y1 == y2 :
        if ymin == y1 :
            print('##7')
            count = 4
        elif ymax == y1 :
            print('##8')
            count = 4
        elif x1 <= xmin <= x2 and x1 <= xmax <= x2 :
            print('##9')
            count=2
        elif x1 <= xmin <= x2 or ((x1 <= xmax <= x2) == False) :
            print('##10')
            count = 1
        elif ((x1 <= xmin <= x2) == False) or x1 <= xmax <= x2 :
            print('##11')
            count = 1
        elif ((x1 <= xmin <= x2) == False) or ((x1 <= xmax <= x2) == False) :
            print('##12')
            count = 1
            

    else :
        
        weight = (y1-y2)/(x1-x2)
        print(weight)
        
        b = y1 - weight * x1
        print(b)
        
        if (y1<= weight * xmin + b <=y2 or y2 <= weight * xmin + b <=y1) and (ymin <= weight * xmin +b <= ymax) :
            count = count + 1

        if (y1<= weight * xmax + b <=y2 or y2 <= weight * xmax + b <=y1) and (ymin <= weight * xmax + b <= ymax) :
            count = count + 1

        if (x1<= (ymin - b)/weight <=x2 or x2 <= (ymin - b)/weight <=x1) and (xmin <= (ymin - b)/weight <= xmax) :
            count = count + 1

        if (x1<= (ymax - b)/weight <=x2 or x2 <= (ymax - b)/weight <=x1) and (xmin <= (ymax - b)/weight <= xmax) :
            count = count + 1
            


    print('#', end='')
    print(test_case, count)
