# print 0!,1!,2!,....n!
n=int(input('Enter'))
for i in range(n+1):
    a = 1

while(i>0):
    a=a*i
    i-=1
    print(a)
