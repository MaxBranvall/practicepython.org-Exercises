# enter name and age
# address a message that tells them
# what year they will turn 100

from datetime import datetime


name = str(input("What is your name? "))
age = int(input("What is your age? "))

dateTime = datetime.now()
year = dateTime.year

diff = 100 - age

oneHun = year + diff

print('Hey {}!\nYou will turn 100 in the year {}!' .format(name, oneHun))

# Ask for another number n
# Print out question n times

question = ("Enter another number! ")

number = int(input(question))

print(('\n'+question) * number)