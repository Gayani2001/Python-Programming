#finding the number of abundants upto given number
number=int(input("Input number: "))

if number>1:
    abundants=0
    for num in range (2,number+1):#taking numbers upto given number
        count=0
        for divisor in range(1,num):#finding proper divisors
            if num%divisor==0:
                count=count+divisor
        
        if count>num:#checking whether sum of proper divisors are greater than the number
            abundants=abundants+1
else:
    print("Invalid Input")

print("Number of abundant numbers from 1 to %i is "% number,abundants)
    
