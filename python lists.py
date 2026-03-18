thislist = ["apple", "banana", "cherry"]
print(thislist)

#Access Listitems

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

# Change List items
thislist = ["apple","banana","cherry","orange","kiwi","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

# Add List Items
thislist = ["apple","banana","cherry"]
thislist.insert(4,"orange")
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

# Remove List items
thislist = ["apple","banana","cherry","banana","kiwi"]
thislist.remove("banana")
print(thislist)

# Loop Lists
thislist=["apple","banana","cherry"]
for i in range (len(thislist)):
    print(thislist[i])

# List Comprehension
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
    print(newlist)

# Sort Lists
thislist = ["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

# Copy Lists
thislist = ["apple","banana","cherry"]
mylist = thislist.copy()
print(mylist)

# Join Lists
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# List Methods
fruits = ['apple','banana','cherry']
cars = ['ford','BMW','Volvo']
fruits.extend(cars)
print(fruits)

#