import random
from decouple import config


INITIAL_MONEY = config('MY_MONEY', default=1000, cast=int)


def play():
    money = INITIAL_MONEY

    while True:
        print(f"Your current money: {money}$")
        slot = input("Choose a slot number from 1 to 30 to place your bet on: ")
        bet = int(input("Place your bet: "))

        if bet > money:
            print("You don't have enough money to place this bet.")
            continue

        winning_slot = random.randint(1, 30)
        print(f"The winning slot is: {winning_slot}")

        if slot == winning_slot:
            money += bet * 2
            print(f"You won {bet * 2}$!")
        else:
            money -= bet
            print("You lost.")

        if money <= 0:
            print("You are out of money. Game over.")
            break

        choice = input("Do you want to play again? (y/n) ")
        if choice.lower() == "n":
            break

play()
