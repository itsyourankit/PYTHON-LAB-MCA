print("Check if a number is even or odd")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even.")
else:
    print(num, "is Odd.")



#chnages

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
