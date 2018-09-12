# Ask user for number
# print appropriate message if it's odd or even

num = int(input("Please enter a number: "))

if num % 2 == 0 and num % 4 == 0:
    print("Even and divisble by 4!")
elif num % 2 == 0:
    print("Just even!")
elif num % 4 == 0:
    print("Just divisible by 4")
else:
    print("Odd!")

num = int(input("Enter a number to check: "))
check = int(input("Enter a number to check with: "))

if num % check == 0:
    print("Divisble!")
else:
    print("Not divisble")