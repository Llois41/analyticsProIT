lucky_number = 10
guess_onetime = input("Willst Du nur einmal raten, Kollege? Tippe y für ja: ")

def guessFunc(guessCount):
    guessed_right = False
    while guessCount>0 and not guessed_right:
        guess = input("Rate mal: ...")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not an int!")
        if guess == lucky_number:
            print("Richtig geraten, Glueckwunsch")
            guessed_right = True
        else:
            guessCount = guessCount-1

if guess_onetime == 'y':
    guess_onetime = True
else:
    guess_onetime = False

if guess_onetime:
    guessFunc(1)
else:
    guessFunc(10000000)