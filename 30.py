def show(lists):
    for i in lists:
        print(i)

def form(one,difference,end):
    lists=[]
    for i in range (0,end):
        lists.append(one+i*difference)
    return lists

show(form(int(input("первый член ")),int(input("разница ")),int(input("колличество членов "))))