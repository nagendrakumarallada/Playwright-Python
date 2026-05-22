print(len(input("enter name ")))

print(len(input("Enter the Series of Numbers ")))


numbers = input("Enter numbers separated by space: ")

numbers_list = numbers.split()

total = sum(map(int, numbers_list))

print("Sum of numbers:", total)

# Lists #
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

# tuple #
coordinates = (17.3850, 78.4867)

print(coordinates)
# sets #
numbers = {1,2,3,3,4}

print(numbers)

# Dictionaries #
employee = {
    "name": "Nagendra",
    "id": 101,
    "role": "Developer"
}

print(employee["name"])