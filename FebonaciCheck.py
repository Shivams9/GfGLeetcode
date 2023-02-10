# # 0! + 1! + 2! +...(n - 2)! + (n - 1)! + n!
# def is_fibonacci(n):
#     a, b = 0, 1
#     while b < n:
#         a, b = b, a + b
#     return b == n
#
# num = int(input("Enter a number: "))
# if is_fibonacci(num):
#     print(num, "is a Fibonacci number")
# else:
#     print(num, "is not a Fibonacci number")

n = int(input("x=\n"))

if n == 0 or n == 1:
    print("Yes")
else:
    a, b = 0, 1
    while True:
        c = a + b
        if c >= n:
            break
        a = b
        b = c
    if n == c:
        print("Yes")
    else:
        print("No")
#