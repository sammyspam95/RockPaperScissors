import random

objects = ['ROCK', 'PAPER', 'SCISSORS']
won = False


def calculate_win(p_input, c_input):  # p for player, c for computer
    global won
    if p_input == c_input:
        return 'D'
    if (p_input == 'ROCK' and c_input == 'SCISSORS') or \
            (p_input == 'PAPER' and c_input == 'ROCK') or \
            (p_input == 'SCISSORS' and c_input == 'ROCK'):
        won = True
        return 'P'
    else:
        won = True
        return 'C'


while not won:
    p = input("Rock, Paper, Scissors: ").upper()
    if p not in objects:
        print("You can't guess that!")
        continue
    c = objects[random.randint(0, 2)]
    print("Computer Guesses " + c.lower().capitalize())
    w = calculate_win(p, c)
    if w == 'P':
        print("You Win!")
    if w == 'C':
        print("Computer Wins!")
