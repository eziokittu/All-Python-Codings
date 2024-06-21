import random as r

# variables
minRange = 400
maxRange = 410
minNum = 1
maxNum = 1000
currentItemCount = 0
currentSum = 0
currentAverage = 0
currentList = []
listItemCount = 0
n = r.randint(4,15) # n = no of list items

def listItemRandomness(currentAverage, noOfItems): 
    num = 0
    minDiff = minRange - minNum
    maxDiff = maxNum - maxRange
    chance = r.randint(1,100)
    if chance<=50:
        num = r.randint(minNum, minRange)
    elif chance>50:
        num = r.randint(maxRange, maxNum)
    return num

# Entering the random int numbers to the current List
for i in range(1,n+1):
    currentList.append(listItemRandomness(currentAverage, i))
    currentSum = 0
    currentAverage = 0
    print(str(currentItemCount) + ".", currentList[i-1])
    listItemCount = currentList.count()
    for j in range(0, listItemCount):
        currentSum += currentList[j]
    currentAverage = currentSum / listItemCount
    currentItemCount +=1

print("Sum =", currentSum)
print("Average =", currentSum/currentItemCount)