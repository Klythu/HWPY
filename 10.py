import random
rework=int(input('введите число монет '))
count=0
for i in range(0,rework) :
    herb=random.randint(0,1)
    if (herb==1):
        count+=1
        print("орел")
    else:
        print("решка")

if count >= rework/2:
    print("перевернуть "+ str(rework-count) + " решек")
else:
    print("перевернуть "+ str(count) + " орлов")