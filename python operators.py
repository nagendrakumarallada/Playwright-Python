# Arithmatic Operator
from ftplib import print_line

x = 150
y = 15
z= 25.188

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Assignment Operator
numbers = [1,2,3,4,5]

if (count:= len(numbers))>3:
    print(f"List has {count} elements")

# Comparison Operator
a=35
b=48

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Logical Operator
print(a<5 or a>50)

# Identity Operator
m = ["apple","banana"]
n = ["apple", "banana"]
p=m

print(m is p)
print(m is n)
print(m == n)
print(m is not n)

# Membership Operator

fruits = ["apple","banana","cherry"]

print("pineapple" not in fruits)

for i in range(10):
    print(i)

print("hello world")

count = 0
while count < 5:
    print(count)
    count+=1

print("Cognine")

for d in range(5):
    if d == 3:
        break
    print(d)

for d in range(5):
    if d == 2:
        continue
    print(d)

print("Programming")
# Bitwise Operators
print(6 ^ 3)

#Operator Precedence
print(5+4-7+3)

