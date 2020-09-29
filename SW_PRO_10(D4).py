T = int(input())

for test_case in range(1, T + 1):
    xmin, ymin, xmax, ymax = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    line = []
    result = []
    new = []
    count = 0

    if x1 == x2 :
        if xmin == x1 :
            print('##1') # x=0 과 일치
            count = 4
        elif xmax == x1 :
            print('##2') # x=xmax와 일치
            count = 4

        else :
            
            line.append([x1, ymin])
            line.append([x1, ymax])
            for i in range(2) :
                if xmin <= line[i][0] <= xmax and ((y1 <= line[i][1] <= y2) or (y2 <= line[i][1] <= y1)) and (ymin <= line[i][1] <= ymax) :
                    result.append(line[i])

            print(result)
            count = len(result)
        
        
    elif y1 == y2 :
        if ymin == y1 :
            print('##7')# y=0 과 일치
            count = 4
        elif ymax == y1 : # y=ymax와 일치
            print('##8')
            count = 4
        else :
            
            line.append([xmin, y1])
            line.append([xmax, y1])
            for i in range(2) :
                if ymin <= line[i][1] <= ymax and ((x1 <= line[i][0] <= x2) or (x2 <= line[i][0] <= x1)) and (xmin <= line[i][0] <= xmax) :
                    result.append(line[i])

            print(result)
            count = len(result)

    else :
        
        weight = (y1-y2)/(x1-x2)
        print(weight)
        
        b = y1 - weight * x1
        print(b)

        
        
        
        line.append([xmin, weight * xmin + b])
        line.append([xmax, weight * xmax + b])
        line.append([(ymin - b)/weight, ymin])
        line.append([(ymax - b)/weight, ymax])
        
        print(line)
        for i in range(4) :
            if ((x1 <= line[i][0] <= x2) or (x2 <= line[i][0] <= x1)) and xmin <= line[i][0] <= xmax and ymin <= line[i][1] <= ymax and ((y1 <= line[i][1] <= y2) or (y2 <= line[i][1] <= y1)) :
                result.append(line[i])
                

        
        for v in result :
            if v not in new :
                new.append(v)

        count = len(new)
        
        
            


    print('#', end='')
    print(test_case, count)
