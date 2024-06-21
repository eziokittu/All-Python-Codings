import random as r

# variable initializations
gameList = ("snake","water","gun")
myScore = 0
computerScore = 0
currentRound = 1
totalNoOfRounds = 10
choiceErrors = 0

# game info
print("----------------snake----------------water----------------gun----------------")
print("Rules : -- snake drinks water -- -- water destroys gun -- -- gun kills snake -- ")
print("Choose any 1 of the 3 and lets see who wins - you or the computer")
print("----------------snake----------------water----------------gun----------------")

# game loop
while currentRound <= totalNoOfRounds:
	# getting the number of rounds
	print("Round -", currentRound)
	currentRound +=1
	currentRoundError = False

	# getting the choices
	computerChoice = r.choice(gameList)
	myChoice = ""
	myCh = input("Your choice : ")
	if myCh == "snake" or myCh == "s" or myCh == "1" or myCh == "snak":
		myChoice = "snake"
	elif myCh == "water" or myCh == "w" or myCh == "2" or myCh == "wat":
		myChoice = "water"
	elif myCh == "gun" or myCh == "g" or myCh == "3" or myCh == "gn":
		myChoice = "gun"
	elif myChoice not in gameList:
		currentRoundError = True
		currentRound -= 1
		print("ERROR! Please type 'snake' or 'water' or 'gun' ")
	print("Computer :", computerChoice)

	# checking who wins the round if no errors in round
	if currentRoundError == False:
		if myChoice == computerChoice:
			print("----- Round Draw -----")
		elif myChoice == "snake" and computerChoice == "water":
			print("----- You score -----")
			myScore += 1
		elif myChoice == "water" and computerChoice == "gun":
			print("----- You score -----")
			myScore += 1
		elif myChoice == "gun" and computerChoice == "snake":
			print("----- You score -----")
			myScore += 1
		else:
			print("----Computer scores----")
			computerScore += 1
		print("")

print("My Score =", myScore, "   Computer Score =", computerScore)
if myScore > computerScore:
	print("You Win\n")
elif myScore < computerScore:
	print("You Lose\n")
elif myScore == computerScore:
	print("Draw\n")