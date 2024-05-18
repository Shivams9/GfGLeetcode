#impelement a program that swaps the values of two variables
def Swap(a,b):
    a,b=b,a
    return a,b
a=5
b=15
a,b= Swap(a,b)
print(a,b)

#Method 2
a=int(input('Enter a number : '))
b=input('Enter String : ')
c=2460
d="Topper"
a,b=c,d
print("Swapping a,b to d, c :", 'Number 1:', a, 'String 2 :',b)
