def my_function():
    print("First Function Program in Python")
my_function()
my_function()
my_function()

# Without Functions
temp1=77
celsius1= (temp1-32) * 5/9
print(celsius1)

temp2 = 95
celsius2 = (temp2-32) * 5/9
print(celsius2)

temp3 = 50
celsius3 = (temp3-32) * 5/9
print(celsius3)

# With Functions
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32) * 5/9
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))

# Return Values - Function that return value
def get_greeting():
    return "First Python Program"
message = get_greeting()
print(message)

# Using the return value directly
def get_greeting():
    return "First Python return Program"
print(get_greeting())

# Pass
def my_function():
    pass

#Function Arguments
def my_function(fname):
    print(fname+" Notification")
my_function("Email")
my_function("Text")
my_function("Video")

# Parameters Vs Arguments
def my_function(name):
    print("Python", name)
my_function("Program")

# Number of Arguments
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("Virat","Kohli")
my_function("Suresh","Raina")

# Default Parameter values
def my_function(name="friend"):
    print("Hi",name)
my_function("John")
my_function()
my_function("Bravo")

# Example
def my_function(country = "Norway"):
    print("I am from", country)
my_function("India")
my_function("Australia")
my_function()

# Keyword Arguments
def my_function(animal,name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function(animal="dog", name="Buddy")

# Example
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(name = "Buddy", animal = "dog")

# Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("Cat", "Pluffy")

# Example - Shift the order
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function("Pluffy", "cat")

#Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)
my_function("Horse", name = "Badsha", age = 5)

#Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# Example
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Jacks", "age": 25}
my_function(my_person)

# Return Values
def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)

#Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#A function that returns a tuple:
def my_function():
  return (10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)

# Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)
my_function("Chris")

#With , /, you will get an error if you try to use keyword arguments:
#def my_function(name, /):
 # print("Hello", name)
#my_function(name = "Emil")

# Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)
my_function(name = "John")

# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:
# Example
def my_function(name):
  print("Hello", name)
my_function("David")

# Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)
result = my_function(5, 10, c = 55, d = 20)
print(result)
result = my_function(5, 10, c = 25, d = 80)
print(result)
result = my_function(5, 10, c = 75, d = 20)
print(result)

#Python *args and **kwargs
#Arbitrary Arguments - *args
def my_function(*kids):
  print("The youngest child is " + kids[3])
my_function("Hari", "Ram", "Sai", "Ravi")

#Accessing individual arguments from *args:
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Sai", "Ravi", "Hari")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Sai", "Ravi", "Hari")

# A function that calculates the sum of any number of values:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5,127))

#Finding the maximum value:
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num
print(my_function(3, 7, 2, 9, 1))

