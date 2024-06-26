from higher_lower_data import data
import higher_lower_art
import random
import os

score = 0
game_should_continue = True
account_b = random.choice(data)


# Format the account data into a printable format
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower count and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Make the game repeatable
while game_should_continue:

    # Generate a random account
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(higher_lower_art.vs)
    print(f"Against: {format_data(account_b)}.")

    # Ask for a user guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    os.system("cls")
    print(higher_lower_art.logo)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, wrong. Final score: {score}")

# TODO: 1. Check it out
