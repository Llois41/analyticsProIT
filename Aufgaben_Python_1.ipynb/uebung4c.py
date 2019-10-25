lucky_number = 10
guess_count = input("Wie oft willst Du raten? ")
try:
    guess_count = int(guess_count)
except ValueError:
    print("That's not an int!")

def guessFunc(guess_count):
    guessed_right = False
    while guess_count>0 and not guessed_right:
        guess = input("Rate mal: ...")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not an int!")
        if guess == lucky_number:
            print("Richtig geraten, Glueckwunsch")
            guessed_right = True
        else:
            guess_count = guess_count-1

if isinstance(guess_count, int):
    guessFunc(guess_count)


