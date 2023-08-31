def All_divide(num):
    flag=1
    i=1
    count=0
    first_list=[]
    second_list=[]
    while flag:
        if num%i==0:
            first_list.append(i)
            second_list.append(int(num/i))
            count+=2
        if first_list[len(first_list)-1]==second_list[len(second_list)-2] :
                first_list.pop()
                second_list.pop()
                flag=0
        i=i+1
        if first_list[len(first_list)-1]==second_list[len(second_list)-1]:
             first_list.pop()
             flag=0
             count-1
    second_list.reverse()
    first_list.extend(second_list)
    
    return first_list

sum=int(input("сумма чисел "))
multy=int(input("произведение чисел "))
candidats=All_divide(multy)
flag=0
for i in range(0,len(candidats)):
     secondCandidat=sum-candidats[i]
     for j in range(0,len(candidats)):
          if secondCandidat==candidats[j]:
               print(secondCandidat," ",candidats[i])
               flag=1
               break
     if flag== 1:
        break

               