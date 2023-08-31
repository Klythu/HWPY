def full_array(len_array,inform):
    tmp_list=[]
    for i in range(0,len_array):
            tmp_list.append(int(input(inform)))
    return tmp_list

def intersection_arr(array_1,array_2):
    if len(array_1)>len(array_2):
        array_1,array_2=array_2,array_1
    res_array=[]
    count=0
    for i in array_1:
         if i in array_2 and not(i in res_array):
            res_array.append(i)
            count+=1          
    return res_array        

Len_1=int(input("Введите размер первой последовательности чисел "))
Len_2=int(input("Введите размер второй последовательности чисел "))
arr_1=full_array(Len_1,'член перврй последовательности ')
arr_2=full_array(Len_2,'член второй последовательности ')
print(sorted(intersection_arr(arr_1,arr_2)))