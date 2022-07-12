import os
import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return print("It's a tie"), play_again()

    #  r > s, s > p, p > r
    if is_win(user, computer):
        #print("You won!")
        return print("You won!"), play_again()

    return print("You lost!"), play_again()


def is_win(player, opponent):
    #  r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def play_again():
    user = input("Would you like to play again? 'y' yes, 'n' no\n")
    if (user == "y"):
        return print(play())
    return quit()


print(play())
os.system('pause')
