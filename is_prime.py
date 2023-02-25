#checking the given is prime or not
while True:
    number=int(input())
    if number<0:#prime numbers are not defined for negatives
        break
    
    if number==1:#1 is not a prime number
        is_prime=0
    else:
        is_prime=1
        for num in range(2,int(number**0.5)+1):
            if number%num==0:
                is_prime=0
                break
            
    if is_prime:
        print("prime")
    else:
        print("non-prime")
        
    
