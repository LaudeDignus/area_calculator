import math
separator="="*35
print(f"{separator}\n\tArea Calculator 📐\n{separator}")

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

while True:
    try:
        choice=int(input("Which shape : "))
    except ValueError:
        print("⚠️  Error: Invalid entry. Please enter a number.")
        continue
    area=None
    if choice==1:
        height = float(input("Give the height : "))
        base = float(input("Give the base : "))
        area = (height*base)/2
    elif choice==2:
        length = float(input("Give the length : "))
        width = float(input("Give the width : "))
        area = length*width
    elif choice==3:
        side = float(input("Give the side : "))
        area = side**2
    elif choice==4:
        radius = float(input("Give the radius : "))
        area = math.pi * (radius**2)
    elif choice==5:
        print("Good Bye 👋🏾")
        break
    else :
        print("Invalid choice. Please select a number between 1 and 5.")
        continue

    print(f'The area is {area}')
