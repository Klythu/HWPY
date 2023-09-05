def dedeli(leters):
    nums=''
    numbers=[]
    res=[]
    simd=[]
    for i in leters:
        flag=True
        if i=='-' or i=='+' or i=='/' or i=='*':
            simd.append(i)
            nums+=' '
            flag=False
        if flag:
            nums+=i
    numbers=nums.split()
    for i in range(0,len(numbers)):
        res.append(numbers[i])
        if i<len(simd):
            res.append(simd[i])
    return(res)


def order(lisst,flag=1):
    if len(lisst)==1:
        res=lisst[0]
        return(int(res))
    if '+' in lisst or '-' in lisst:
        for i in range(1,int(len(lisst)/2+1)):
            if lisst[i*2-1]=='+':
                lefts=[]
                rights=[]
                for j in range(0,i*2-1):
                    lefts.append(lisst[j])
                for j in range(i*2,len(lisst)):
                    rights.append(lisst[j])
                    print(lefts,rights)
                if flag==1:
                    return (order(lefts,flag=1)+order(rights,flag=1))
                return(order(lefts,0)-order(rights,0))
                
            if lisst[i*2-1]=='-':
                lefts=[]
                rights=[]
                for j in range(0,i*2-1):
                    lefts.append(lisst[j])
                for j in range(i*2,len(lisst)):
                    rights.append(lisst[j])
                    print(lefts,rights)
                if flag==1:
                    return (order(lefts,flag=0)-order(rights,flag=0))
                return(order(lefts,0)+order(rights,0))
    if '*' in lisst or '/' in lisst:
        for i in range(1,int(len(lisst)/2+1)):
            if lisst[i*2-1]=='*':
                lefts=[]
                rights=[]
                for j in range(0,i*2-1):
                    lefts.append(lisst[j])
                for j in range(i*2,len(lisst)):
                    rights.append(lisst[j])
                    print(lefts,rights)
                return (order(lefts)*order(rights))
            if lisst[i*2-1]=='/':
                lefts=[]
                rights=[]
                for j in range(0,i*2-1):
                    lefts.append(lisst[j])
                for j in range(i*2,len(lisst)):
                    rights.append(lisst[j])
                    print(lefts,rights)
                return (order(lefts)/order(rights))
        



eqesion=input()
eqesion_list=dedeli(eqesion)
print(eqesion_list)
print(order(eqesion_list))
