import random as gluk

def create(num):
    listos=[]
    for i in range(0,num):
        tmp=gluk.randint(0,1000)
        listos.append(tmp)
    print(listos)
    return(listos)

def search_place(listos,min,max):
    place=[]
    for i in listos:
        if i<max and i>min :
            place.append(listos.index(i))#через счётчик надёжнее, но не зря же этот метод есть
    return(place)

print(search_place(create(int(input("размер массива "))),int(input("минимальное число")),int(input("максисальное число "))))