a = 35
b = 70
while True:
    c = a % b
    if c == 0:
        print(b)
        break
    a = b
    b = c
# print(a,'mod',b,'reminder=',c)
#
