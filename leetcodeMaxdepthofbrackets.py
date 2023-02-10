s='(1+(2*3)+((8)/4))+1'
n=len(s)
# print(n)
stack=[]
max=0
for ch in s:
    if ch=='(':
        stack.append(ch)
        if len(stack)>max:
            max=len(stack)
        continue
    if ch==')':
        stack.pop()
print(max)


# a=[1,2,3,4,5]
# max=0
# n=len(a)
# for i in range(0,n,1):
#     if a[i]>max:
#         max=a[i]
# print(max)
