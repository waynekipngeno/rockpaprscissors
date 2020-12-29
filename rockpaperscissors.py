import random
import sys

print('ROCK PAPER SCISSORS')
gameResults = {'wins':0, 'losses':0, 'draws':0}

def gameMechanics(playerMove):
    message = ''
    choices = ['r', 's', 'p']
    compMove = random.choice(choices)
    if playerMove.lower() == compMove:
        gameResults['draws'] += 1
        message = 'It\'s a draw! You and the computer picked {}'.format(playerMove)
    elif playerMove == choices[0] and compMove == choices[1]: 
        gameResults['wins'] += 1
        message = 'You win! You picked {} and the compter picked {}'.format(playerMove, compMove)
    elif playerMove == choices[0] and compMove == choices[2]:
        gameResults['losses'] += 1
        message = 'You lose! You picked {} and the compter picked {}'.format(playerMove, compMove)
    elif playerMove == choices[1] and compMove == choices[0]:
        gameResults['losses'] += 1
        message = 'You lose! You picked {} and the compter picked {}'.format(playerMove, compMove)
    elif playerMove == choices[1] and compMove == choices[2]:
        gameResults['wins'] += 1
        message = 'You win! You picked {} and the compter picked {}'.format(playerMove, compMove)
    elif playerMove == choices[2] and compMove == choices[0]:
        gameResults['wins'] += 1
        message = 'You win! You picked {} and the compter picked {}'.format(playerMove, compMove)
    elif playerMove == choices[2] and compMove == choices[1]:
        gameResults['losses'] += 1
        message = 'You lose! You picked {} and the compter picked {}'.format(playerMove, compMove)
        
    return message
def playGame(): 
    playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit:\n')
    if playerMove == 'q':
        sys.exit()
    else:
        print(gameMechanics(playerMove))



while True:
    print(gameResults)
    playGame()