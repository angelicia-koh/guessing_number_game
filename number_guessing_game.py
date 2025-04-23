import random

def guessing_game():
    number = random.randint(1,100)
    guess_count = 0

    while True:
        guess = input("Guess a number between 1-100: ")

        if not guess.isdigit():
             print("Invalid input")
             continue #skip to the next loop iteration
        
        guess = int(guess) # so instead of "guess = int(input("Guess a number between 1-100: "))"
                           # if you initialize it here, you can check and avoid ValueError message
                           # and you must initalize it because operations can only work with ingeters
        guess_count += 1

        if guess > number: 
             print("Lower!")           
        
        elif guess < number:
             print("Higher!")

        else:
            print("Yay! You guessed it!!!!!!")
            print("\nYou got the answer after", guess_count, "times!\n")
            break

guessing_game()
