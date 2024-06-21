# Webisite - Hackerrank
#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true



# Problem Statement
# A valid email address meets the following criteria:
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is , , or  characters in length.
# Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
# Hint: Try using Email.utils() to complete this challenge. For example, this code:



n = int(input())
arr = []
emailsAllowed = []
allowed = "abcdefghijklmnopqrstuvwxyz"
allowed += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allowed2 = "0123456789"
allowed2 += ".-_"
for i in range(n):
    arr.append(input().split())
for i in range(n):
    emailNotAllowed = False
    extensionLength = 0
    start = 0
    for ch in arr[i][1]:
        if ch=="<":
            start = 1
        elif start==3 and ch==">":
            if emailNotAllowed == False:
                emailsAllowed.append(arr[i])
        elif start == 1:
            if (arr[i][1][1] not in allowed):
                emailNotAllowed = True
            if (ch not in allowed and ch not in allowed2):
                if (ch == "@"):
                    start = 2
                else:
                    emailNotAllowed = True
        elif start == 2:
            if (ch not in allowed):
                if (ch == "."):
                    start = 3
                else:
                    emailNotAllowed = True
        elif start == 3:
            if ch in allowed and extensionLength<4:
                extensionLength += 1
            else:
                emailNotAllowed = True

for email in emailsAllowed:
    print(email[0], email[1])
