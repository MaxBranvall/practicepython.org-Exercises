# Make a two player rock-paper-scissors game

gameOn = True
moves = ['rock', 'paper', 'scissors']

while gameOn:

    player1 = int(input('Player 1\nType 0 for rock, 1 for paper, and 2 for scissors: \n'))
    player2 = int(input('Player 2\nType 0 for rock, 1 for paper, and 2 for scissors: \n'))

    player1 = moves[player1]
    player2 = moves[player2]

    if (player1 == 'rock' and player2 == 'paper'):
        print('player 2 wins')

    elif (player1 == 'paper' and player2 == 'rock'):
        print('player 1 wins')

    elif (player1 == 'rock' and player2 == 'scissors'):
        print('player 1 wins')

    elif (player1 == 'scissors' and player2 == 'rock'):
        print('player 2 wins')

    elif (player1 == 'paper' and player2 == 'scissors'):
        print('player 2 wins')

    elif (player1 == 'scissors' and player2 == 'paper'):
        print('player 1 wins')

    # print(player1, player2)
    gameOn = False
