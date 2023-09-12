def print_operation_table(operation, num_rows=6, num_columns=6):
    mas=[0]*num_rows
    for i in range(num_rows):
        mas[i]=[0]*num_columns
    for i in range (1,1+num_rows):
        for j in range (1,1+num_columns):
            mas[i-1][j-1]=operation(i,j)
    for i in mas:
        print(i)


print_operation_table(lambda x,y:x*y)