#Finbonacci Series
n=int(input('Enter Number'))
a=0
b=1
count=0
if n<=0:
    print('Not Valid number')
elif n==1:
    print(n)
    print(a)
else:
    print('fibonacci Series')
    while count<n:
        print(a)
        nth=a+b
        a=b
        b=nth
        count+=1
    

    
