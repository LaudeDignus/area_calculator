import math
style="="*35
print(f"{style}\n\tArea Calculator 📐\n{style}")

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

shape=0
while shape!=5:
    shape=int(input("Which shape : "))
    if shape==1:
        height = int(input("Give the height : "))
        base = int(input("Give the base : "))
        area = (height+base)/2
        print(f'The area is {area}')
    elif shape==2:
        length = int(input("Give the length : "))
        width = int(input("Give the width : "))
        area = length*width
        print(f'The area is {area}')
    elif shape==3:
        side = int(input("Give the side : "))
        area = side**2
        print(f'The area is {area}')
    elif shape==4:
        radius = int(input("Give the radius : "))
        area = math.pi * (radius**2)
        print(f'The area is {area}')
    else:
        print("Good Bye 👋🏾")