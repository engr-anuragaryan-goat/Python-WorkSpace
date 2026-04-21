"WAP to sort a list of tuples using lambda."

#declearing a list of tuples
lst=[('English',88),('Science',90),('Maths',97),('Social Science',82)]

#applying logic to short the the list
result=lambda seq:sorted(seq)

print("The sorted list of tuples :",result(lst))
