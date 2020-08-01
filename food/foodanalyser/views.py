from django.shortcuts import render
import pandas as pd
from .knn  import findnearest

def login(request):
    return render(request,'login.html')

def firstpage(request):
    if(request.method=='POST'):
        usedata=pd.read_csv('/home/kavya/Desktop/project/food/files/userinfo.csv')
        users=list(usedata['username'])
        ages=list(usedata['age'])
        cusine=list(usedata['preference'])
        age=0
        location=''
        areadyordered=[]
        locations=list(usedata['location'])
        odered=list(usedata['already_ordered'])
        for i in range(len(users)):
            if users[i]==request.POST['uname']:
                age=ages[i]
                location=locations[i]
                alreadyordered=odered[i].split(',')
                preferences=list(map(int,cusine[i].split(',')))
            
        x=findnearest(age,location,preferences)
        value=x[0]
        prefer=x[1]
        vallist=[]
        for k in value:
            if len(value[k])!=0:
                vallist.append(value[k])
        vallist=sum(vallist,[])
        print(vallist)
        preferlist=[]
        for k in prefer:
            if len(prefer[k])!=0:
                preferlist.append(prefer[k])
        preferlist=sum(preferlist,[])
        print(preferlist)


        logdata=pd.read_csv('/home/kavya/Desktop/project/food/files/log.csv')
        u=list(logdata['usernames'])
        p=list(logdata['passwords'])
        
        for i in range(len(u)):
            if(request.POST['uname']==u[i] and request.POST['psw']==p[i]):
                return render(request,'firstpage.html',{'values':vallist,'preference':preferlist})
            # else:
        return render(request,'login.html')



def search(request):
    if request.method=="POST":
        s=request.POST['search']
        hasdata=pd.read_csv('/home/kavya/Desktop/project/food/files/foodandhotels.csv')
        dish=list(hasdata['ord1'])
        dish1=list(hasdata['ord2'])
        res=list(hasdata['resname'])
        dicter=[]
        for i in range(len(dish)):
            if dish[i]==s:
                dicter.append({"hotel":res[i],"dish":dish[i]})
            if dish1[i]==s:
                dicter.append({"hotel":res[i],"dish":dish1[i]})
            if res[i]==s:
                dicter.append({"hotel":res[i],"dish":dish[i]})
        return render(request,'search.html',{"search":dicter})

            

    
            
  

