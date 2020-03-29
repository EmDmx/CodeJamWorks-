def reader(): 
    lines =int(input())
    full=[]
    
    #print(lines)
    for i in range(1,lines+1):
        line1 = [int(s) for s in input().split(" ")]
        numberOfStacks=line1[0]
        stacklist=[]
        for j in range(0,numberOfStacks):
            stack = [int(s) for s in input().split(" ")]
            stacklist.append(stack)
        full.append([line1,stacklist])
    #print(full)
    return full

def drPatel(table):
    
    beautyPoint = []

    for item in table :
        numberOfStacks=item[0][0]
        #lenOfStacks=item[0][1]
        platesToTake=item[0][2]
        points=0
        
        for attempt in range(platesToTake):
            firstMax=0
            '''
            for i in range(len(item[1])):
                if item[1][i][0]>firstMax: 
                    firstMax =item[1][i][0]
                    firstStackNo=i
            '''
            for firstvalue in item[1]:
                if len(firstvalue) > 0 :
                    if firstvalue[0]> firstMax: 
                        firstMax = firstvalue[0]
                        firstStackNo = item[1].index(firstvalue)
                else : 
                    continue
            maxes=[]
            means=[]
            indexes =[]
            plates=1
            for stack in item[1]:
                if stack  :
                    stackMax = max(stack)
                    totals =0
                    index=1
                    for value in stack:                    
                        if value == stackMax: 
                            break
                        else: 
                            totals+=value
                            index+=1
                            plates+=1
                    indexes.append(index)
                    maxes.append(totals)
                    means.append(totals/plates)
            #    else :
            #        means.append(stack[0])
            #        maxes.append(stack[0])
            maxMean=max(means)
            maxMeanIndex= means.index(maxMean)
            
            #print("maxmean",maxMean)
            if  maxMean > firstMax: 
                points+= max(maxes)
                item[1][maxMeanIndex] = item[1][maxMeanIndex][:indexes[maxMeanIndex]]
                platesToTake = platesToTake-plates-1
                #print("here")
            else: 
                #print("firstmax",firstMax)
                points+=item[1][firstStackNo][0]
                item[1][firstStackNo].pop(0)
                platesToTake-=1
                #print("here2")
            '''
            for t in range(len(means)): 
                if means[t]> firstMax:
                    points+=maxes[t]
                    item[1][t] = item[1][t][:indexes[t]]
                    platesToTake -= plates
                    print("here4")
                else: 
                    points+=item[1][firstStackNo][0]
                    item[1][firstStackNo].pop(0)
                    platesToTake-=1
                    print("here")
            '''
        beautyPoint.append(points)
    return beautyPoint
def printer(cases): 
    for i in range(len(cases)):
        print('Case #{}: {}'.format(i+1,int(cases[i])))
    
                
if __name__=="__main__": 
    table =reader()
    values = drPatel(table)
    printer(values)