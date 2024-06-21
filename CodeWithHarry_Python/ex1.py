# Create a dictionary and
# take input from the user
# and return the meaning of
# the word from the dictionary

# A class named "dictionary" having two fundamental data types: string, string
class dictionary:
    def __init__(self, _word, _meaning):
        self.word = _word
        self.meaning = _meaning

# Custom Function
def dic1():
    """This is supposed to be a function that takes both meaning and definition from the user and then asks the user if they want to enter more data. Then finally it prints the dictionary."""

    d1 = {} #Creating an object "d1" of the class "dictionary"

    # loop will run until the user wants no more words to insert in the dictionary
    while(True):
        d1[input("Tell the word for that meaning : ")] = input("\nExplain the meaning : ")

        # this "more" vaiable gets the string input
        more = input("Want to enter more data to the dictionary (default: NO) ? (y for YES) : ")

        if (more.lower() != 'y'):
            break

    print("\nPrinting the dictionary : ") 
    for key, value in d1.items():
        print(str(key) + " : " + str(value), end = "\n")

    print("\n")

# This is the required code defined as a function
def dic2():
    d2 = {
        "lol" : "Laugh Out Loud",
        "np" : "No Problem",
        "gn" : "Good Night",
        "afk" : "Away From Keyboard"
    }
    userInput = input("Enter the word to know it's meaning : ")
    for i in d2:
        if userInput == i:
            s1 = "--- '" + userInput + "' means '" + d2.get(userInput) + "'. ---"
            print(s1.center(80, "-"), end="\n\n")
            return 0
    s2 = "The word '" + userInput + "' is not defined in the dictionary"
    print(s2.center(80,"-"), end="\n\n")

# the program starts from here
if __name__=="__main__":
    #print(dic1.__doc__)
    #dic1() 
    dic2()