import random

directory = "D:\Coding Stuff, Editing\Visual Studio Python Codings\MyProjects\Miscellaneous\Assets/"
fileName = "FindTheNumberGame2_Score.txt"

def ShowGameRules():
    s='''
    ----- Find the number Game - II -----
    --- Rules of game ---
    1 - The program generates a random number
    2 - and prompts the user to guess the number
    3 - if the user's guess is below the random number, the random number is divided by 2 else multiplied by 2
    4 - the game ends if the user guesses the exact number
    5 - the number of tries is given as score
    --- Some other parts of this program ---
    1 - after each game ends the score is saved in a text file.
    2 - before starting the game, the user has option to choose the starting and ending numbers and see high scores
    3 - after dividing the secret number if that number becomes float say 6.5 it will become 6
    '''
    print(s)

def SaveToFile(start, end, secret, tries):
    """saves the details of each game in a dedicated file for score"""
    print("Secret =", int(secret), " Number of tries =", tries)
    try:
        scoreFile = open(directory+fileName, "a+")
        scoreFile.write("\n" + str(start) + " " + str(end) + " " + str(int(secret)) + " " + str(tries))
        print("Writing score to file SUCCESS".rjust(60, " "))
        scoreFile.close()
    except:
        print("Failed to find the score file or ERROR in writing to file".rjust(60, " "))
    # scoreFile.write("\n"+"Starting and Ending number ("+str(start)+","+str(end)+
    #  ") "+ " Secret = "+str(int(secret))+" Number of Tries = "+str(tries))
    GameMenu()

def ShowScore():
    """reads all high scores from the file which saves all the high scores"""
    try:
        scoreFile = open(directory + fileName, "r")
    except:
        scoreFile = open(directory + fileName, "a+")
        print("File Creation SUCCESS".rjust(60, " "))
    scores = scoreFile.readlines()
    print("")
    print("".center(60, "-"))
    print(" Showing previos Scores ".center(60, "-"))
    print("|  Starting and Ending number |   Secret   | No. of Tries  |")
    print("".center(60, "-"))
    for s in scores:
        n = s.split()
        start, end, secret, tries = n[0], n[1], n[2], n[3]
        print("|", end="")
        print(("(" + start + "," + end + ")").center(29, " "), end="|")
        print(secret.center(12, " "), end="|")
        print(tries.center(15, " "), end="|")
        print("")
    print("".center(60, "-"))
    scoreFile.close()
    GameMenu()

def Game():
    print("")
    print(" Find the number game : II ".center(60, "-"))
    startNumber = 0
    endNumber = 0
    try:
        startNumber = int(input("Enter range start : "))
        endNumber = int(input("Enter range end : "))
    except:
        print("[ The numbers you entered must be an INTEGER ] Try Again from Start -------------")
        return 0
    secret = random.randrange(startNumber, endNumber + 1)
    guessIsCorrect = False
    numberOfTries = 0
    while not guessIsCorrect:
        try:
            guess = int(input("Guess : "))
            numberOfTries += 1
            if guess == int(secret):
                SaveToFile(startNumber, endNumber, secret, numberOfTries)
                guessIsCorrect = True
            elif guess < int(secret):
                secret = int(secret) / 2
                print("The secret number got divided by 2! (secret number was bigger than your guess)")
            elif guess > int(secret):
                secret = int(secret) * 2
                print("The secret number got multiplied by 2! (secret number was smaller than your guess)")
        except:
            print("The guess number needs to be an INTEGER. Guess Again!")

def GameMenu():
    print("")
    print(" Game Menu ".center(60, "-"))
    print("Insert '1' for START, '2' for HIGH SCORES, '3' to EXIT --- ", end="")
    choice = input()
    if choice == "1":
        Game()
    elif choice == "2":
        ShowScore()
    elif choice == "3":
        print(" Thanks for playing. Made by Bodhisatta Bhattacharjee. ".center(60, "-"))
        print(" END of GAME ".center(60, "-"), end="\n\n")

if __name__ == "__main__":
    ShowGameRules()
    #directory = input("Enter the directory where the score file will be saved - ")
    GameMenu()
