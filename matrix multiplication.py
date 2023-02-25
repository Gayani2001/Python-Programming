##matrix multiplication

#read the elements of a matrix
def read_matrix(rows,columns):
    matrix_list=[]
    try:
        for row in range(rows):
            row_i=input()
            
            row_list=list(map(int,row_i.strip().split(" ")))
            if len(row_list)!=columns:#number of elements in a row is not equal to given number
                return
            else:
                matrix_list.append(row_list)
        return matrix_list
    except:#other errors
        return "Error"

#transpose of a matrix
def transpose(mat_list):
    matrix_list=[]
    for j in range (len(mat_list[0])):
        row_list=[]
        for i in range(len(mat_list)):
            element=mat_list[i][j]
            row_list.append(element)
        matrix_list.append(row_list)
    return matrix_list

#multiplying two matrices
def multiply(mat1,mat2):
    if len(mat1[0])!=len(mat2):#number of columns in first matrix is not equal to number of rows in second matrix
        return
    else:
        matrix_list=[]
        for i in range(len(mat1)):
            row_list=[]
            for j in range(len(mat2[0])):
                total=0
                for num in range(len(mat1[0])):
                    element=mat1[i][num]*mat2[num][j]
                    total=total+element
                row_list.append(total)
            matrix_list.append(row_list)
        return matrix_list

#display the resultant matrix
def display(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()

#taking dimensions
dimensions=input("Enter the dimension: ")
dimension=list(map(int,dimensions.strip().split(",")))
n=dimension[0]
m=dimension[1]

print("Enter Matrix A: ")
matrixA=read_matrix(n,m)
if matrixA==None:
    print("Invalid Matrix")
elif matrixA=="Error":
    print("Error")
    
else:
    print("Enter Matrix B: ")
    matrixB=read_matrix(n,m)
    if matrixB==None:
        print("Invalid Matrix")
    elif matrixB=="Error":
        print("Error")
        
    else:
        transposeB=transpose(matrixB)
        
        output=multiply(matrixA,transposeB)
        
        if output==None:#can't multiply the two matrices
            print("Error")
        else:
            display(output)
