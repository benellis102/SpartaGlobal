from random import randint

list = ['rock', 'paper', 'scissors']
computer = list[randint(0, 2)]
player = False

while player == False:
    player = input('rock, paper or scissors? ')
    if player == computer:
        print("it's a tie!\n")


    elif player == 'rock':
        if computer == 'paper':
            print('paper beats rock, you lose!\n')
        else:
            print('rock beats scissors, you win!\n')


    elif player == 'paper':
        if computer == 'scissors':
            print('scissors beats paper, you lose!\n')
        else:
            print('paper beats rock, you win!\n')


    elif player == 'scissors':
        if computer == 'rock':
            print('rock beats scissors, you lose!\n')
        else:
            print('scissors beat paper, you win\n')

    else:
        print('please enter a valid choice\n')

    player = False
    computer = list[randint(0, 2)]

