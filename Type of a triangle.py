#find the type of a triangle
angle1=int(input('Enter angle 1: '))
angle2=int(input('Enter angle 2: '))
angle3=int(input('Enter angle 3: '))
#checking whether traingle or not
if angle1+angle2+angle3==180:
    if angle1>angle2:
        if angle1>angle3:
            max_angle=angle1
        else:
            max_angle=angle3
    else:
        if angle2>angle3:
            max_angle=angle2
        else:
            max_angle=angle3
    if max_angle>90:
        print("Obtuse angled")
    elif max_angle==90:
        print("Right angled")
    else:
        print("Acute angled")
else:
    print("Angles do not form a triangle")
           
