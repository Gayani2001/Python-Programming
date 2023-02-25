#total and average mark
students=[]
for num in range(4):
    try:
        marks=input()
        mark_list=list(map(int,marks.strip().split(' ')))#convert marks into integers and put it into a list
        students.append(mark_list)
    except:
        pass
for student in students:
    total=0
    for mark in student:
        total=total+mark
    average=round(total/len(student),1)
    print("Total:",total,end=" ")
    print("Average:",average)
        

