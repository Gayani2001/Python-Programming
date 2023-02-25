#encrypting a given message
message=input("Enter message: ")
base=int(input("Enter base: "))

if 1<base<=10:
    output=''
    for letter in message:
        ascii_number=ord(letter)#obtaining ASCII value
        
        base_number=''
        while ascii_number!=0:
            remainder=ascii_number%base
            ascii_number=ascii_number//base
            
            base_number=str(remainder)+base_number#obtaining ASCII number from the given base
            
        output=output+base_number
print(output)
