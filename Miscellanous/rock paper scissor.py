# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:17:18 2021

@author: Narayan soni
"""
"""
Implements the game of Rock-Paper-Scissors!

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(I promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
#rock paper scissors


import random

N_GAMES = 3

def main():
    Estimated_score = 0
    print_welcome()
    for i in range(N_GAMES):
        HUMAN_INPUT = GET_HUMAN_INPUT()
        AI_INPUT = GET_AI_INPUT()
        WINNER = FIND_WINNER(AI_INPUT, HUMAN_INPUT)
        print('The AI played: ',AI_INPUT)
        print('WINNER is: ',WINNER)
        Estimated_score += GET_SCORE(WINNER)
    print('Your score is:',Estimated_score)


def GET_AI_INPUT():
    ai_input = random.randint(1,3)
    if ai_input == 1:
        return 'rock'
    elif ai_input == 2:
        return 'paper'
    elif ai_input == 3:
        return 'scissors'

def GET_HUMAN_INPUT():
    while True:
        my_input = input('what do you play? ')
        if my_input == 'rock' or my_input == 'paper' or my_input == 'scissors':
            return my_input
        print('Enter a valid input')


def FIND_WINNER(ai_move, human_move):
    if ai_move == human_move:
        return 'NO ONE , its a tie'
    if ai_move == 'rock':
        if human_move == 'scissors':
            return 'ai'
        return 'human'
    if ai_move == 'scissors':
        if human_move == 'paper':
            return 'ai'
        return 'human'
    if ai_move == 'paper':
        if human_move == 'rock':
            return 'ai'
        return 'human'
    print('should not get here!')

def GET_SCORE(WINNER):
    if WINNER == 'human':
        return 1
    elif WINNER == 'ai':
        return -1
    return 0


def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()