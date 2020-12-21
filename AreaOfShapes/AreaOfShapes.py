area = 0
pi = 3.147

def AreaShape(x):

    if(x==1):
        print("YOU HAVE SELECTED SQUARE:")
        a = input("Enter the length of the side of the square: ")
        if(a.isdigit() and float(a) > 0):
            area = float(a)**2
            print("Area of square is : ",area)
        else:
            print("Enter a valid positive integer")

    elif(x==2):
        print("YOU HAVE SELECTED RECTANGLE")
        l = input("Enter the length of the rectangle, enter a positive number: ")
        b = input("Enter the base of the rectangle, enter a positive number: ")
        if(l.isdigit() and b.isdigit() and float(l) > 0 and float(b) > 0):
            area = float(l) * float(b)
            print("The area of the rectangle is : ",area)
        else:
            print("Enter valid positive integers")

    elif(x==3):
        print("YOU HAVE SELECTED TRIANGLE")
        h = input("Enter the height of the triangle, enter a positive integer: ")
        b = input("Enter the base of the triangle, enter a positive integer: ")
        if(h.isdigit() and b.isdigit() and float(h) > 0 and float(b) > 0):
            area = (float(h) * float(b)) * 0.5
            print("Area of Triangle is : ",area)
        else:
            print("Enter a valid positive integers")

    else:
        print("YOU HAVE SELECTED CIRCLE")
        r = input("Enter the radius of the circle: ")
        if(r.isdigit() and float(r) > 0):
            area = pi * (float(r)**2)
            print("Area of the circle is : ",area)
        else:
            print("Enter a valid positive integer")


print('Which shape would you like to calculate the area for: Please select a number')
print('1: Square\n2: Rectangle\n3: Triangle\n4: Circle')

x = int(input("Enter your choice: "))

if((x>0) and (x<5)):
    AreaShape(x)
else:
    print("Enter a valid option")
