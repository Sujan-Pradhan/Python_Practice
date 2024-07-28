from art import logo,vs
from gamedata import data
import random

def format_data(account):
    """ Takes the account data and return the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_description}, from  {account_country}")

def check_answer(guess,a_follower, b_follower):
    """ Take the user guess and follwer counts and returns if they got it right."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_B = random.choice(data)

while game_should_continue:

    account_A = account_B
    account_B = random.choice(data)
    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}.")
    print(vs)
    print(f"Against B: {format_data(account_B)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]


    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(logo)
    if is_correct:
        score += 1
        print (f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")