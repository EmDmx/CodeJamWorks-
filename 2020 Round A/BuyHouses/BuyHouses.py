def reader(): 
    lines =int(input())
    full=[]
    for i in range(1,lines+1):
        line1 = [int(s) for s in input().split(" ")]
        line2 = [int(s) for s in input().split(" ")]
        line3 = [line1,line2]
        full.append(line3)
    return full


def buyer(table):
    cases=[]
    for item in table: 
        counter = 0
        itemNumber=item[0][0]
        budget = item[0][1]
        prices = sorted(item[1])

        for item in prices: 
            if item > budget: 
                break 
            elif item <= budget : 
                budget -=item
                counter+=1
        cases.append(counter)
    return cases

def printer(cases): 
    for i in range(len(cases)):
        print('Case #{}: {}'.format(i+1,int(cases[i])))
    

if __name__=="__main__": 
    table=reader()
    cases=buyer(table)
    printer(cases)