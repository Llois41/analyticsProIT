lucky_number = 10
guess = input("Rate doch mal, was meine Zahl ist ;): ...")
not_guessed = True

try:
    guess = int(guess)
except ValueError:
   print("That's not an int!")

while not_guessed:
    if guess == lucky_number:
        print("Richtig! Kauf Dir nen Keks")
        not_guessed = False
    else:
        guess = input("Leider nicht, rate noch mal :P")
        try:
            guess = int(guess)
        except ValueError:
            print("That's not an int!")