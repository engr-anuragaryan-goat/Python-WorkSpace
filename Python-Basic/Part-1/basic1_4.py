"WAP that calculates the area of a circle based on the redius entered by the user."

#function defination
def area(R):
    return 3.14*R*R

#prompt user to enter the radius of circle
r=float(input("Enter the radius of the circle : "))
ar=area(r)
print("The area of the given circle ; ",ar)
