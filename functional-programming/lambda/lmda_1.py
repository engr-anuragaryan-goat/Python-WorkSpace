"WAP to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda that multiplies argument x with argument y and prints the result"

#part 1
#prompt user to enter a number
n=int(input("Enter a number : "))
sum=lambda x : (x+15)
print("If we add 15 to the given number, then the sum we get isequal to",sum(n))

#part 2
#prompt user to enter two number
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
mul=lambda x,y : (x*y)
print("If we multiply both the inputs then, the product we get isequal to",mul(a,b))
