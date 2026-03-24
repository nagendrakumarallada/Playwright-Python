# Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# duplicates not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# example
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# example
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# example
set1 = {"abc", 34, True, 40, "male"}
print(set1)

# type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Access Set items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# example
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# example
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Add set items
# Add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Set items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# example - discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# example - pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# example - clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# example - delete()
#thisset = {"apple", "banana", "cherry"}
#del thisset
#print(thisset)

# Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join Sets
# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# using "|" instead of union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# using "|"
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# using "&" instead of intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# intersection_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# example
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# using "-" instead of difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# using "^" instead of symmetric_difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# symmetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# FrozenSet
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))