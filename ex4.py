# Take in an int through user input, return a list of divisors for that int
count = 1
user = int(input('Enter a number: '))

divisors = [x for x in range(1, 9999) if user % x == 0]

for num in divisors:
    print('{}: {}' .format(count, num))
    count += 1