import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'''Bagels, a deductive logic game/
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    Whwn I say:     That Means:
        Pico        One digit is correct but in the wrong position
        Fermi       One digit is correct and in the right position
        Bagels      No digit is correct
    
    For example, if the secret number was 248 amd your guess was 843,
    the clues would be Fermi Pico.''')

    while True: # Main game loop
        secret_num = Get_Secret_Num()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it")

        num_guesses = 1

        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until a valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}:")
                guess = input(("> "))
            
            clues = Get_Clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break

            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}")

        # Ask the player if they want to play again
        print("Do you want to play again? (yes or no)")

        if not input(("> ").lower().startswith("y")):
            break
    
    print("Thanks for playing")


def Get_Secret_Num():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''

    numbers = list("0123456789")
    random.shuffle(numbers)

    # Get the first digits in the new sequence for the secret number
    secret_num = ""
    for num in range(NUM_DIGITS):
        secret_num += str(numbers[num])
    
    return secret_num


def Get_Clues(guess, secret_num):
    ''' Returns a string with Pico, Fermi and Bagels clues for a guess.'''

    if guess == secret_num:
        return "You got it!"
    
    clues = []

    for index in range(len(guess)):
        if guess[index] == secret_num[index]:
            clues.append(" Fermi ")
        elif guess[index] in secret_num:
            clues.append(" Pico ")

    if len(clues) == 0:
        return "Bagels"
    else:
        # Sort the clues alphabetically so their original position doesn't give any extra info.
        clues.sort()
        return " ".join(clues)


# If the program is run instead of imported the game is run.
if __name__ == "__main__":
    main()