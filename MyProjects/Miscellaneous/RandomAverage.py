import random as r
import math as m

# User inputs
try:
    print("Set a range to get the average (for wrong input : range = 400 to 410) --")
    averageRangeMin = float(input("Start - "))
    averageRangeMax = float(input("End - "))
except:
    averageRangeMin = 400
    averageRangeMax = 410

# Some variable initializations
totalItemCount = 0
totalSum = 0
totalaverage = 0
n = 0
noOfLists = r.randint(1,5)
stringOfTheListNumbers = ""

def listItemRandomness(list1):
    pass

print("------------------------------------------------------------------------------------------")
print("A random no. of lists (1 to 5).")
print("A list of random numbers (1 to 1000), contained in a list with random length (4 to 15) ---")
print("No. of lists -", noOfLists)
print("------------------------------------------------------------------------------------------", end="\n\n")
for eachList in range(1,noOfLists+1):
    # Initializing some variables
    currentAverage = 0
    currentList = []
    currentItemCount = 0
    currentSum = 0
    n = r.randint(4,15)
    print("n =", n)

    # Entering the random int numbers to the current List
    for i in range(1,n+1):
        # currentList.append(r.randint(1,1000))
        currentList.append(listItemRandomness(currentList))

    # Iterating the current list items
    for listItem in currentList:
        currentItemCount +=1
        print(str(currentItemCount) + ".", listItem)
        currentSum += listItem
        # adding list items as string to the variable
        stringOfTheListNumbers += str(listItem)

    # updating some variables
    totalSum += currentSum
    totalItemCount += currentItemCount

    # Printing
    print("Sum =", currentSum)
    print("Average =", currentSum/currentItemCount)
    print("---------------------------")

print("\n\n      The final Sum  -- ", totalSum)
print("      The final Average  -- ", totalSum / totalItemCount, end="\n\n")