import random as r

mypass_length_min = 8
mypass_length_max = 20

# getting all the numbers
mypass_numbers = ['0','1','2','3','4','5','6','7','8','9']

# getting all the uppercase letters
mypass_letters_upper = []
i=ord("A")
while (ord("Z")-i >= 0):
    mypass_letters_upper.append(chr(i))
    i+=1

# getting all the lowercase letters
mypass_letters_lower = []
i=ord("a")
while (ord("z")-i >= 0):
    mypass_letters_lower.append(chr(i))
    i+=1

# getting all the special characters
mypass_special = ['@','%','+',"\\",'/','\'','!','#','$','^','?',
                  ':',',','(',')','{','}','[',']','-','_','`','~']

# all possible characters that make the password
mypass_allPossible = mypass_special + mypass_letters_lower + mypass_letters_upper + mypass_numbers

count_numbers = 0
count_letters_upper = 0
count_letters_lower = 0
count_special = 0

def CheckPasswordStrength(str,state):
    '''str is the string variable which is being checked
    state = 0 means password entered is being checked
    state = 1 means password is generated and being checked
    Return values 1,2,3,4,5 is used for state 0
    Return values -1,0 is used for state 1'''
    count_numbers = 0
    count_letters_upper = 0
    count_letters_lower = 0
    count_special = 0

    if (len(str) < mypass_length_min) or (len(str) > mypass_length_max):
        if state==0: return 5
        elif state==1: return -1
    else:
        for i in str:
            if ((count_numbers>0) or (i in mypass_numbers)):
                count_numbers = 1
            if ((count_letters_upper>0) or (i in mypass_letters_upper)):
                count_letters_upper = 1
            if ((count_letters_lower>0) or (i in mypass_letters_lower)):
                count_letters_lower = 1
            if ((count_special>0) or (i in mypass_special)):
                count_special = 1
            if i not in mypass_allPossible:
                return 6 # this only works for state 0 

        if (count_numbers == count_letters_upper == count_letters_lower == count_special == 1):
            if state==0: return 1
            elif state==1 : return 0
        elif (count_numbers == 0):
            if state==0: return 2
            elif state==1 : return -1
        elif count_special == 0:
            if state==0: return 3
            elif state==1 : return -1
        elif (count_letters_upper + count_letters_lower <= 0):
            if state==0: return 4
            elif state==1 : return -1
        else:
            if state==0: return 1
            elif state==1 : return 0

        return 1
        
def GenerateStrongPassword():
    newPass_length = r.randint(mypass_length_min, mypass_length_max)
    newPass = ""
    num = 0
    ch = ""

    while True:
        chance1 = r.randint(1,1000)
        temp = len(mypass_special)*len(mypass_letters_upper)*len(mypass_numbers)
        chance2 = r.randint(1, temp-1)
    
        # getting the new password letter by letter
        # numbers
        if ((chance1>0) and (chance1<=250)):
            num = int(chance2/(temp/len(mypass_numbers)))
            ch = str(num)
            newPass += ch
        # uppercase letters
        elif ((chance1>250) and (chance1<=500)):
            num = int(chance2/(temp/len(mypass_letters_upper)))
            ch = mypass_letters_upper[num]
            newPass += ch
        # lowercase letters
        elif ((chance1>500) and (chance1<=750)):
            num = int(chance2/(temp/len(mypass_letters_lower)))
            ch = mypass_letters_lower[num]
            newPass += ch
        # special characters
        elif ((chance1>750) and (chance1<=1000)):
            num = int(chance2/(temp/len(mypass_special)))
            ch = mypass_special[num]
            newPass += ch

        # EXIT CONDITION
        if (newPass_length==len(newPass)):
            if CheckPasswordStrength(newPass,1)==0:
                break
            else :
                newPass_length = r.randint(mypass_length_min, mypass_length_max)
                newPass=""
        elif (len(newPass) > newPass_length):
            newPass_length = r.randint(mypass_length_min, mypass_length_max)
            newPass=""

    return newPass

# end of this script