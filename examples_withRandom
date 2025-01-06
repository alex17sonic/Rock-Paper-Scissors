import random

options = ("Rock", "Paper", "Scissors")
running = True 

while running:
    my_choise = None
    opponent = random.choice(options)
    
    # Check if i have an valid choose
    while my_choise not in options:
        my_choise = input("Choose your option between Rock, Paper or Scissors: ").capitalize().strip()
    
    print(f"Your choice is: {my_choise}")
    print(f"Your opponent's choice: {opponent}")

    # Check the winner
    if my_choise == opponent:
        print("It's a tie!")
    elif my_choise == "Rock" and opponent == "Scissors":
        print("You win!")
    elif my_choise == "Paper" and opponent == "Rock":
        print("You win!")
    elif my_choise == "Scissors" and opponent == "Paper":
        print("You win!")
    else:
        print("Opponent Wins!")

    # Option to play again
    if not input("Play again? y/n: ").lower().strip() =="y":
        running = False

print("Thanks for playing!")
