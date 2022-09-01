from random import randint

print("Welcome to Number guessing game !")
print('Choose your difficulty level : 1.easy 2.hard 3.exit')
level = input()

num = randint(1,100)
chances = {"easy" : 10, "hard" : 5, "exit" : exit}

def choose_level(level):
    if level == "easy":
        print(f"You have {chances[level]} chances to guess")
    elif level == "hard":
        print(f"You have {chances[level]} chances to guess")
    elif level == "exit":
        print("Exiting...")
        exit()
    else:
        print("Please make a choice : easy/hard/exit")
        level = input()
        choose_level(level)

def check_num(guess, num, chances):
    if guess < num:
        print(f"Guess is too low {guess},", end = " ")
        chances[level] -= 1
        print(f"You have {chances[level]} chances to win")
    elif guess > num:
        print(f"Guess is too high {guess},", end=" ")
        chances[level] -= 1
        print(f"You have {chances[level]} chances to win")
    else:
        print("You guessed it right !")
        exit()

def guess_num():
    while(chances[level]):
        guess = int(input("Make a guess : "))
        check_num(guess, num, chances)
        if chances[level] == 0:
            print(f"Sorry, you lost the game, the number is {num}")

choose_level(level)
guess_num()
