def check_win(money):
    if money > INITIAL_MONEY:
        print(f"You won {money - INITIAL_MONEY}$!")
    elif money < INITIAL_MONEY:
        print(f"You lost {INITIAL_MONEY - money}$!")
    else:
        print("You broke even.")
