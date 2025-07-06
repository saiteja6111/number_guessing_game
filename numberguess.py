import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if choice.lower() == 'easy':
    start = True
    finally_number = random.randint(1,100)
    count = 10
    while start:
        if count > 0:
            print(f"You have {count} attempts remaining to guess the number.")
            guess_num = int(input("Make a guess: "))
            if guess_num > finally_number:
                print("Too high. \nGuess again.")
                count = count - 1
            if guess_num < finally_number:
                print("Too low. \nGuess again.")
                count = count - 1
            if guess_num == finally_number:
                print(f"You got it! The answer was {finally_number}")
                start = False
        else:
            print("You've run out of guesses. Refresh the page to run again.")
            start = False
elif choice.lower() == 'hard':
    start = True
    finally_number = random.randint(1,100)
    count = 5
    while start:
        if count > 0:
            print(f"You have {count} attempts remaining to guess the number.")
            guess_num = int(input("Make a guess: "))
            if guess_num > finally_number:
                print("Too high. \nGuess again.")
                count = count - 1
            if guess_num < finally_number:
                print("Too low. \nGuess again.")
                count = count - 1
            if guess_num == finally_number:
                print(f"You got it! The answer was {finally_number}")
                start = False
        else:
            print("You've run out of guesses. Refresh the page to run again.")
            start = False
