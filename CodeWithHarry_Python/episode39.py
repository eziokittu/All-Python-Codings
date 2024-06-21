import random as r
import math as m

totalItemCount = 0
totalSum = 0
totalaverage = 0
n = 0
noOfLists = r.randint(2,4)
stringOfTheListNumbers = ""

print("------------------------------------------------------------------------------------------")
print("A random no. of lists (2 to 4).")
print("A list of random numbers (1 to 1000), contained in a list with random length (4 to 15) ---")
print("No. of lists -", noOfLists)
print("------------------------------------------------------------------------------------------", end="\n\n")
for eachList in range(1,noOfLists+1):
    # Initializing some variables
    currentList = []
    currentItemCount = 0
    currentSum = 0
    n = r.randint(4,15)
    print("n =", n)

    # Entering the random int numbers to the current List
    for i in range(1,n+1):
        currentList.append(r.randint(1,1000))

    # Iterating the current list items
    for listIem in currentList:
        currentItemCount +=1
        print(str(currentItemCount) + ".", listIem)
        currentSum += listIem
        # adding list items as string to the variable
        stringOfTheListNumbers += str(listIem)

    # updating some variables
    totalSum += currentSum
    totalItemCount += currentItemCount

    # Printing
    print("Sum =", currentSum)
    print("Average =", currentSum/currentItemCount)
    print("---------------------------")

print("\n\n      The final Sum  -- ", totalSum)
print("      The final Average  -- ", totalSum / totalItemCount, end="\n\n")