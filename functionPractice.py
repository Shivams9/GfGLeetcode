def passByValue(a):
    a= 2*a
def passByReference(a):
    a.append(10)
def factorial(n):  #Recursive
    if n<=0:
        return 1
    return n * factorial(n - 1)
x=2
passByValue(x)
print(x)
x=[]
passByReference(x)
print(x)
print(factorial(6))
