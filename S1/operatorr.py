a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operators ---")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")

print("\n--- Assignment Operatos ---")
c = a
print(f"Initial value of c: {c}")
c += b
print(f"c += b -> {c}")
c -= b
print(f"c -= b -> {c}")
c *= b
print(f"c *= b -> {c}")
c /= b
print(f"c /= b -> {c}")



def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i  in range(2, n):
        result = result * i

    return result

N = int(input("Enter a Non-negative integer: "))
print(f"The factorial of {N} is {factorial(N)}")