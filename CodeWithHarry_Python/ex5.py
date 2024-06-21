# Health Management System

# Directory for the files where they will be created
dir = "CodeWithHarry_Python/assets/"

# 2 functions
def getdate():
    '''Function to give a time stamp'''
    import datetime
    return datetime.datetime.now()

def choices():
    '''Function to ask the user to input 3 choices - returns 0 if wrong input is taken,
    returns 11,12,21,22,31,32,41,42 for retrieving , or 1000+ these numbers to update the client's info'''
    print("\nPress 1 to [retrieve 'food' or 'exercise' for any client'] OR Press 2 to [update the client's information]")
    choice1 = input()
    if choice1 == "1":
        print("Whose diet/exercise do you want to check : ")
        choice2 = input("Select 1 for Harry, 2 for Rohan, 3 for Hammad, 4 for Robin : ")
        choice3 = input("Now select 1 for diet, 2 for exercises : ")
        try:
            if (int(choice2)>=1 or int(choice2)<=4) and (int(choice3)==1 or int(choice3)==2):
                return (int(choice2)*10)+int(choice3)
            else:
                return 0
        except:
            return 0
    elif choice1 == "2":
        print("Whose diet/exercise do you want to update : ")
        choice2 = input("Select 1 for Harry, 2 for Rohan, 3 for Hammad, 4 for Robin : ")
        choice3 = input("Now select 1 for diet, 2 for exercises : ")
        try:
            if (int(choice2)>=1 and int(choice2)<=4) and (int(choice3)==1 and int(choice3)==2):
                return (int(choice2)*10)+int(choice3) + 1000
            else:
                return 0
        except:
            return 0
    else:
        return 0

userWantsToContinue = True
while userWantsToContinue:
    userWantsToContinue = False
    mychoice = choices()

    if mychoice == 0:
        print("You might not have chosen a valid choice. You need to restart the program again.\n")

    else:
        currentFile = None

        if mychoice<1000: # for checking the information already present in the file
            try:
                currentFile = open(dir + "ex5_" + str(mychoice%1000) + ".txt", "r+")
                lines = currentFile.readlines()
                print("") # 1 line gap
                for line in lines:
                    print(line, end="")
                currentFile.close()
            except:
                print("No such files exist yet. You need to create it.")

        elif mychoice>1000: # for updating the file
            currentFile = open(dir + "ex5_" + str(mychoice%1000) + ".txt","at+")
            wantToAddMore = True
            while wantToAddMore:
                update_the_file = input("Enter what you want to add to the file -\n")
                currentFile.write("\n["+str(getdate())+"] "+ update_the_file + "")
                if input("Do you want to add more (1 for yes , any other key for no) : ") != "1":
                    wantToAddMore = False
            currentFile.close()

    choice0 = input("\nPress '1' to continue OR any other key to exit from the program : ")
    if choice0 == "1":
        userWantsToContinue = True
    else:
        print("End-Of-Program".center(80,"-"))
        userWantsToContinue = False