#matrix transpose
matrix_list=[]
invalid=0
error=0
while True:
    rows=input()
    if rows=='-1':#end of taking inputs
        break
    try:
        row_list=list(map(int,rows.strip().split(" ")))#transfer every element to integers
        matrix_list.append(row_list)
        if len(row_list)!=len(matrix_list[0]):
            invalid=1
            print('Invalid Matrix')
            
  
    except:
        error=1
        print("Error")
        
    
if invalid==0 and error==0:
    new_list=[]
    for column in range(len(matrix_list[0])):#taking transpose
        new_row=[]
        for row in range(len(matrix_list)):
            element=matrix_list[row][column]
            new_row.append(element)
        new_list.append(new_row)
    
    for new_row in new_list:
        for new_column in new_row:
            print(new_column,end=" ")
        print()
else:
    pass

    
