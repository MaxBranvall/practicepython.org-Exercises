# Take two list of differing sizes each contianing a random set of numbers.
# Write the program to return a list containing only the common numbers between both lists.
import random

lista = list(range(1, 101))
listb = [num*2 for num in lista if num*2 < 100]

listc = [num for num in listb if num in lista]

print('Original')
print(listc)

# 1. Randomly generate two lists

lista = random.sample(range(1, 1000), 50)
listb = random.sample(range(1, 1000), 100)

listc = [num for num in lista if num in listb]

print('Extra 1')
print(listc)

# 2. Write this in one line

listc = [num for num in (random.sample(range(1, 1000), 50)) if num in (random.sample(range(1, 1000), 100))]

print('Extra 2')
print(listc)

def keyPress():
    