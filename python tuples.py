# Tuple Creation
thistuple = ("apple","banana","cherry")
print(thistuple)

# Tuples - Data types
tuple1 = ("apple","banana","cherry")
tuple2 = (1,3,5,7,9)
tuple3 = (True,False,True)
print(tuple1,tuple2,tuple3)

# Length of tuple
print(len(tuple1))
print(len(tuple2))
print(len(tuple3))

# Not a Tuple
tuplex = ("apple")
tupley = (1)
tuplez = (True)
print(type(tuplex))
print(type(tupley))
print(type(tuplez))

# Access Tuple
# 1. Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# 2. Negative Indexing
thistuple = ("apple","banana", "cherry")
print(thistuple[-3])

# 3. Range of Indexes
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])

# example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[3:])

# Update Tuples
# 1. Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# 2. Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# 3. Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# example
#thistuple = ("apple", "banana", "cherry")
#del thistuple
#print(thistuple)

# Unpack Tuple
# 1. Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# 2. Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# example
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop Tuples
# 1. Loop through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# 2. Loop Through the Index Numbers
thistuple = ("mango", "melon", "orange")
for i in range(len(thistuple)):
  print(thistuple[i])

# 3. Using a While Loop
thistuple = ("grape", "kiwi", "papaya")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Tuples
# 1. Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# 2. Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 5
print(mytuple)