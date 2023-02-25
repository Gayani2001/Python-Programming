#calculate electricity bill
units=int(input("Enter the Units: "))
if units<=60:
    if units<=30:
        amount=units*2.50+30
    else:
        amount=30*2.50+(units-30)*4.85+60
else:
    if units<=90:
        amount=60*7.85+(units-60)*10+90
    elif units<=120:
        amount-60*7.85+30*10+(units-90)*27.75+480
    elif units<=180:
        amount=60*7.85+30*10+30*27.75+(units-120)*32+480
    else:
        amount=60*7.85+30*10+30*27.75+60*32+(units-180)*45+540
print(amount)
