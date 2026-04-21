"WAP to create a function that takes one argument, and that argument will be multiplied with an unknown given number"

#function defination that takes one argument
def take(n):
    return lambda x:x*n
result=take(2)
print("Double the number of 15 : ",result(15))
result=take(3)
print("Tripal the number of 15 : ",result(15))
result=take(4)
print("Quadruple the number of 15 : ",result(15))

