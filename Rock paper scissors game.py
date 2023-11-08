print("~~Rock,Paper,Scissors Game~~")
import random

def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return f"It's a tie! You both chose {player_choice}."
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return f"You win! {player_choice} beats {computer_choice}."
    else:
        return f"You lose! {computer_choice} beats {player_choice}."

# Main program
print("Welcome to Rock, Paper, Scissors!")
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
result = play_game(player_choice)
print(result)
