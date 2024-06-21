import random

secretWords = ["banana", "apple","guava","avocado","cherry"
    ,"mango","watermelon"]
secretWord = random.choice(secretWords)

print("----------------------Guess the words GAME--------------------")
print("Guess letter/s or word from a to z (lowercase only) : ")
print("The word can be any of these - ",end="")
for word in secretWords:
    print(word, end=" ")

tries = 102
lettersGuessedCorrectly = []
guess = ''
while True:
    guess = input("\nGuess : ")

    if (guess == secretWord):
            print("You guessed the correct word")
            print("Your Score -", tries)
            break

    if (guess.isalpha()):
        #print("Letter is alphabet")
        if guess in secretWord:
            print("Correct Letter/s!")
        else:
            print("Wrong Letter!")
        tries-=2

    else:
        print("Not alphabet/s! Try Again!")
        continue
print("----------------------------------------------------------")
