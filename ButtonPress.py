#THIS SOLUTION PASSES BOTH TEST CASES FOR SMALL AND LARGE DATASETS.


#This is a specific method to this question. It gets values and combinations and adds them into dict. 
#By adding them a dict I can use them like object.
def reader():
    t =int(input())
    pref= []
    cases = { }
    for i in range(1,t+1):
        n,p = [int(item) for item in input().split(" ")]
        #print('Those are numbers to print {} :  {} {}'.format(i,n,p))
        for j in range(p):
            pref.append(input())
        
        cases[i] = {'N' :n, 'P' : p, 'Pref': pref }
        #To clean pref for new case I declare it again. 
        pref=[]
    #print(cases)
    return cases,t
def bruteSol(case,t):
    for i in range(1,t+1): 
        # This part gets the necessary fields from the objects
        total=case[i]['N']
        pref= case[i]['Pref']
        #In total we have 2**total amount of combination possibilities with 2 buttons.
        total_opp= 2**total
        #I needed a constant total_opp so I created another variable with same value.
        tops=total_opp
        loss=0
        #I made it set and list to get rid off same combinations
        pref= list(set(pref))
        pref= sorted(pref)
        #In this part I check if one combination contains other inside. To not make redundant reducement in possibilities.
        for n in range(len(pref)):
            for zz in range(n+1,len(pref)):
                #if pref[zz].startswith(pref[n]):
                if pref[n] == pref[zz][:len(pref[n])]:
                    pref[zz]=pref[n]
        # I make it set again to get rid off redundant combinations
        pref = list(set(pref))
        #print(pref)
        
        #In this part I traverse through the prefix list and reduce the amount of combinations from total.
        for _ in pref :
            loss= total_opp / 2**len(_)
            tops-= loss
            if tops<=0: 
                tops=0
                break
           # print('Loss : {}'.format(loss))
        print('Case #{}: {}'.format(int(i),int(tops)))

#-----  I WILL BE UPDATING THE CODE TO ADD TRIE SOLUTION.

if __name__ == "__main__":
    case,t=reader()
    bruteSol(case,t)


