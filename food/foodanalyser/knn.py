import pandas as pd


def findnearest(age,location,preferences):
    print(age,location)
    dictage={x:[] for x in range(0,50)}
    hasdata=pd.read_csv('/home/kavya/Desktop/project/food/files/foodandhotels.csv')
    # print(hasdata)
    ages=list(hasdata['age'])
    
    locations=list(hasdata['location'])
    
    resnames=list(hasdata['resname'])
    
    orders1=list(hasdata['ord1'])
    
    orders2=list(hasdata['ord2'])
  
    review1=list(hasdata['rev1'])
    
    review2=list(hasdata['rev2'])
    cusine1=list(hasdata['cusine1'])
    print(cusine1)

    cusine2=list(hasdata['cusine2'])
    prefer={x:[] for x in range(0,50)}
    for i in range(1,50):
        
        diff=abs(age-i)
        #print(location,locations[i])
        if locations[i]==location:
            print(location)
            if(((review1[i]+review2[i])/2)>3.00):
                dictage[diff].append({"orders":[orders1[i],orders2[i]],"restaurant names":[resnames[i]]})
        if cusine1[i] in preferences:
            prefer[diff].append({"orders":[orders1[i],orders2[i]],"restaurant names":[resnames[i]]})
    return [dictage,prefer]
        
print(findnearest(16,'velachery',[1,2]))