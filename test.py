print(len(input("enter name ")))

print(len(input("Enter the Series of Numbers ")))


numbers = input("Enter numbers separated by space: ")

numbers_list = numbers.split()

total = sum(map(int, numbers_list))

print("Sum of numbers:", total)