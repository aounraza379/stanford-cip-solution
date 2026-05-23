import random

NUM_ROUNDS = 5

def main():

    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0

    for i in range(NUM_ROUNDS):
        # Milestone #4: Play multiple rounds
        print(f'Round {i+1}')

        # Milestone #1: Generate the random numbers
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        print(f"Your number is {user_number}")

        # Milestone #2: Get user choice
        user_guess = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension #1: Safeguard user input
        while not (user_guess == 'higher' or user_guess == 'lower'):
            user_guess = input("Please enter either higher or lower: ")

        # Milestone #3: Write the game logic
        higher_and_correct = (user_guess == 'higher') and (user_number > computer_number)
        lower_and_correct = (user_guess == 'lower') and (user_number < computer_number)

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Milestone #5: Adding a points system and a thank you!

        print(f"Your score is now {score}")
        print()
    print("Thanks for playing!")

    # Extension #2: Conditional ending messages
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()