# Ask the user for a string and print out whether it is a palindrome

userString = str(input('Enter a word: '))

def checkForPalindrome(x):

    x = x.split()
    x =''.join(x)
    
    if (x[::-1] == x):
        print(f'Original: {x}')
        print(f'Reversed: {x[::-1]}')

        print('That\'s a palindrome!')
    else:
        print(f'Original: {x}')
        print(f'Reversed: {x[::-1]}')

        print('Not a palindrome :(')      
    


checkForPalindrome(userString)
