import random
hard_level_turns = 5
easy_level_turns = 10
print("Welcome to the Number Guessing Game")
print("I'm thinking of the number between 1 and 100")
number = random.randint(1,100)
def check(guess_answer,actual_answer,turns):
    if guess_answer > actual_answer:
        print("Too High")
        return turns - 1
    elif guess_answer < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"you got it! actual answer {actual_answer}")

def set_difficulty():
    level = input("Enter you choice of level 'easy' or 'hard: ")
    if level.lower() == 'easy':
        return easy_level_turns
    elif level.lower() == 'hard':
        return hard_level_turns
turns = set_difficulty()
guess = 0   
while guess != number: 
    print(f"You have {turns} attempts remaoning to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check(guess,number,turns)


