#maximum and minimum
#numbers=input()
numbers="0 0 0 0 0"
num_list=numbers.strip().split(" ")
maximum=num_list[0]
minimum=num_list[0]
for num in num_list:
    if float(num)>float(maximum):#finding maximum
        maximum=num
    if float(num)<float(minimum):#finding minimum
        minimum=num
print("Minimum =",minimum)
print("Maximum =",maximum)
