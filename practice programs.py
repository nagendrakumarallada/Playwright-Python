# Simple Calculator
a = int(input())
b = int(input())
op = input("Enter operator: ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)

# Login Check
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Even or Odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Largest of the Given Numbers
a, b, c,d,e,f,g = 10, 25, 15,56,101,2,35
print(max(a, b, c,d,e,f,g))

# Sum of Numbers
n = int(input())
print(sum(range(1, n+1)))

# Multiplication Table
n = int(input())
for i in range(1, 41):
    print(n, "x", i, "=", n*i)

# Reverse a string
text = input()
print(text[::-1])

# Vowels count
text = input()
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print(count)

# Factorial
n = int(input())
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

# Prime Numbers
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Remove Duplicates
lst = [1,2,2,3]
print(list(set(lst)))