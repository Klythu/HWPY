import random
berry_list_len=random.randint(3,20)
berry_list=[]
berry_list_culc=[]
for i in range(0,berry_list_len):
    berry_list.append(random.randint(1,1000000))
for i in range(0,berry_list_len):
    if i-1<0:
        berry_list_culc.append(berry_list[i]+berry_list[i+1]+berry_list[len(berry_list)-1])
    elif i+1>len(berry_list)-1:
        berry_list_culc.append(berry_list[i]+berry_list[1]+berry_list[i-1])
    else:
        berry_list_culc.append(berry_list[i]+berry_list[i+1]+berry_list[i-1])
berry_list_culc.sort
print(berry_list,berry_list_culc,berry_list_culc[len(berry_list_culc)-1])