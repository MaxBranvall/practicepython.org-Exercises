# 1. Print out all the elements of a given list that are less than 5.
origList = [1, 3, 4, 5, 7, 9, 10, 14]

for num in origList:
    if (num <= 5):
        print (num)
    else:
        continue

# 2. Same as above, but make a new list out of said elements and print the list.
origList = [1, 3, 4, 5, 7, 9, 10, 14]
newList = []

for num in origList:
    if (num <= 5):
        newList.append(num)
    else:
        continue
    
print(newList)

# 3. Write number 2 in one line
origList = [1, 3, 4, 5, 7, 9, 10, 14]

newList = [num for num in origList if num <= 5]

print(newList)

# 4. Ask for an int from the user and return a list containing elements from the original
# list that are smaller than the users chosen int.
origList = [1, 3, 4, 5, 7, 9, 10, 14]

user = int(input('Enter a number: '))

newList = [num for num in origList if num < user]

print(newList)