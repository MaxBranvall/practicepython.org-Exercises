# Using list comprehension, make a new list containing only the even numbers from list a.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]

print(b)