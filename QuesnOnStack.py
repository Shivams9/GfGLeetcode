#--deye hue string me se (b+c) print krna aur pura string print kro..

expression='(a+(b+c)-d)'
n=len(expression)
stack=[]
for i in range(n):
    ch=expression[i]        #ch me expression ka start to end tk store keya
    if ch=='(':             #agar ch ya i ko open ( ye mila toh wahi usko khali stack me bhej denge
        stack.append(i)
        continue
    if ch==')':             #loop me hi ch ya i ko close ')' bracket mile to uske bich ka value print kre
        outposition=stack.pop()     #outpos name se object leke usme stack ki value ko pop karenge
        print(expression[outposition:i+1])         #expression k andr outpos tk aur i YA ch 1kam tak value dega esleye iko+ 1 kar denge
