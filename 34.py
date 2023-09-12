data=input('фраза товарища Винни: ')
data=data.split(' ')
data=list(map(lambda x: x.count('а'),data))
if data==filter(lambda x: x==data[0],data):
    print('Парам пам-пам  ')
else:
    print('Пам парам')
print(data)