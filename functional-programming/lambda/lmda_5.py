"WAP to filter a list of integers using lambda"

#global variables
result1=[]
result2=[]

#defining a function
def fltr(dta):
    if dta%2==0:
        result1.append(dta)
    else:
        result2.append(dta)
lst=[1,2,3,4,5,6,7,8,9,10]
map(fltr,lst)
print(result1,'\n\n',result2)














