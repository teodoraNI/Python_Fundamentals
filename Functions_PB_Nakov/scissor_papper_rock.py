import random

quit_or_play = 'yes'
tuple1 = ('scissor', 'rock', 'paper')
count_comp_wins = 0
count_player_wins = 0
def print_results(w, p, c):
    print(f"{w} won!\n  current score: \n    computer's wins: {c}\n    player's wins: {p}")

while quit_or_play == 'yes':
    player_move = input("Chose [paper], [rock] or [scissor]: ")
    if player_move not in tuple1:
        raise SystemExit("Invalid input! Try again!")
    computer_move = random.choice(tuple1)
    print(f"Computer's choice is: {computer_move}")
    if computer_move == player_move:
        print('draw')
    elif computer_move == 'rock':
        if player_move == 'scissor':
            count_comp_wins += 1
            print_results('Computer', count_player_wins, count_comp_wins)
        else:
            count_player_wins += 1
            print_results('Player', count_player_wins, count_comp_wins)
    elif computer_move == 'paper':
        if player_move == 'rock':
            count_comp_wins += 1
            print_results('Computer', count_player_wins, count_comp_wins)
        else:
            count_player_wins += 1
            print_results('Player', count_player_wins, count_comp_wins)
    elif computer_move == 'scissor':
        if player_move == 'paper':
            count_comp_wins += 1
            print_results('Computer', count_player_wins, count_comp_wins)
        else:
            count_player_wins += 1
            print_results('Player', count_player_wins, count_comp_wins)
    quit_or_play = input("Type [yes] to play again or [no] to quit: ")
    if quit_or_play == 'no':
        raise SystemExit("Thanks for playing!")




