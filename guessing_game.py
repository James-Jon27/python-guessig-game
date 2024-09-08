import random

print("Welcome to the Guessing Game!\n")

def min_max():
    while True: ##* replaced recursion with while loop to avoid None error
        mn = input("What is the minimum number? ")
        mx = input("What is the maximum number? ")
        try:
            mn_num = int(mn)
            mx_num = int(mx)
            if mn_num >= mx_num:
                print("Minimum must be less than Maximum")
            else:
                return (mn_num, mx_num)
        except ValueError:
            print("I only take numbers for minimum and maximum...\n")
            #* min_max()  


minimum, maximum = min_max()

secret_num = random.randint(minimum, maximum)

print(f"\nI'm thinking of a number between {minimum} and {maximum}...")


def difficulty():
    while True:
        g = input("Select Difficulty\n(E)asy, (M)edium, or (H)ard: ").lower()
        if g == "e":
            g = 5
        elif g == "m":
            g = 3
        elif g == "h":
            g = 1
        else:
            print("Please type E, M, or H to select difficulty...\n") 
        return g

def game(gc, gss):
    while gc < gss:
        guess = input(f"\nGuess #{gc + 1}: ")
        try:
            int(guess)
        except ValueError:
            print("Guess must be a number!\nYou have lost a turn >:(")
            gc += 1
            continue

        gc += 1

        if int(guess) == secret_num:
            print("You Win!")
            break
        elif gc != gss:
            output = "Nope!"
            output += (
                " My number is lower..."
                if int(guess) > secret_num
                else " My number is higher..."
            )

            print(output)
    else:
        print(f"You LOSE!!!\n\nMy number was {secret_num}\n")


guess_count = 0
guesses = difficulty()

game(guess_count, guesses)
