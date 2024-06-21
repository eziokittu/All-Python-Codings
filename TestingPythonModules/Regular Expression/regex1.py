import re

string = '''This is 1 string to be tested
Hello I am "Ravi" I'm 24 years old
My email: helloIndia@gmail.com'''
print_str_length1 = 60
print_str_length2 = 90
# Testing all the module methods in regular Expression

def regex_notes():
    '''Some basic Notes of Regular Expression - and methods defined are used here'''
    print(" Regex Functions ".center(print_str_length2,"-"))
    l = r'''
    - search() -
    search the regular expression pattern and return the first occurrence.
    it will check all lines of the input string. returns a match object
    when the pattern is found and “null” if the pattern is not found

    - findall() -
    module is used to search for “all” occurrences that match a given pattern.
    findall() will iterate over all the lines of the file and will
    return all non-overlapping matches of pattern in a single step.

    - match() -
    will search the regular expression pattern and return 
    the first occurrence. The Python RegEx Match method checks 
    for a match only at the beginning of the string. So,
    if a match is found in the first line, it returns the match object. 
    But if a match is found in some other line,
    the Python RegEx Match function returns null.

    - sub() -
    function replaces the matches with the text of your choice
    Example1: text = "Hello World Good Night"
    text = re.sub("\s", "9", text)
    # text = "Hello-World-Good-Night"
    4th parameter can be a count - no. of chararcters to change
    Example2: text = "Hello World Good Night"
    text = re.sub("[a-z]", "-", txt, 5)
    # text = "T__ ___n in Spain" changes upto 5 letters

    - split() -
    this re.split() is quite same as default split()
    it can have a 3rd parameter to split upto that no. of occurences

    Match object
    can be handled by using re.span() - creates a tuple of all hte match objetcs,
    re.string() - creats a string of all the match objects,
    re.group() - creates a list of all the match objects

    --------------------- NOTE ---------------------
    1. search() and match() returns a match object
    2. findall() returns a list
    3. use group() to remove the match object and get the values inside of it
    example : print(re.search(r"...",string).group())
    ------------------ END OF NOTE------------------'''
    for i in l.split("\n"):
        print(i.center(print_str_length2))

def regex_metaCharacters():
    ''' all the meta characters of Regulae Expression are used here'''

    print(" Meta Characters ".center(print_str_length2,"-"))
    # '.' Dot is the default mode
    # matches any character except newline
    print("Using '.'".center(print_str_length1,"-"))
    print(re.search(r"...",string))
    print(re.findall(r"a",string))
    print(re.search(r"...................",string).group())


    # '[ ]' - A set of characters, e.g. [amk] will match 'a', 'm', or 'k'
    # [a-z] will match any lowercase ASCII letter, [0-5][0-9] will match all the 
    # two-digits numbers from 00 to 59, and [0-9A-Fa-f] will match any hexadecimal digit.
    print("\n"+"Using '[ ]'".center(print_str_length1,"-"))
    print(re.findall("[a-z]",string))
    print(re.findall("[0-9]",string))
    print(re.findall("[0-5][0-9]",string))
    print(re.findall("[0-9A-Fa-f]",string))


    # '^' - matches the expression to the right, at the start 
    # of a string before it experiences a line break
    # [ NOTE - This matches only the start of the string ]
    print("\n"+"Using '^'".center(print_str_length1,"-"))
    print(re.match("^This is",string)) # returns a MATCH object
    print(re.match("^This is",string).group())
    print(re.search("^1 string",string))


    # '$' - string ends with the expression - Matches the end of the string
    # or just before the newline at the end of the string
    # and in MULTILINE mode also matches before a newline
    print("\n"+"Using '$'".center(print_str_length1,"-"))
    print(re.search("tested$",string))
    print(re.search("old$",string))


    # '*' - Causes the resulting RE to match 0 or more repetitions of
    # the preceding RE, as many repetitions as are possible. ab* will
    # match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s. 
    print("\n"+"Using '*'".center(print_str_length1,"-"))
    print(re.findall("s*",string))
    print(re.findall("12*","312121 333 12222 31123"))


    # '+' - Causes the resulting RE to match 1 or more repetitions of
    # the preceding RE. ab+ will match ‘a’ followed by any
    # non-zero number of ‘b’s; it will not match just ‘a’.
    print("\n"+"Using '+'".center(print_str_length1,"-"))
    print(re.findall("s.+g",string)) # means - starts with s, ends with g,
    # and in betwee n there is atleast 1 letter
    s = "12 102 1002 11002"
    print(re.findall("1+2",s))
    print(re.findall("1+..2",s))
    print(re.findall("11+..2",s))
    # print(re.findall("12*","121212 12222 112"))
    # print(re.findall("12*","121212 12222 112"))


    # '?' - zero or one occurence - Causes the resulting RE to match 0 or 1
    # repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.
    print("\n"+"Using '?'".center(print_str_length1,"-"))
    print(re.findall("stri?ng",string))
    print(re.findall("str?.ng",string))
    print(re.findall("st?.ng",string)) # none - 2 letters in between


    # "{ }" - Exactly the specified number of occurrences
    # Matches whatever regular expression is inside the parentheses,
    # and indicates the start and end of a group
    print("\n"+"Using '{}'".center(print_str_length1,"-"))
    print(re.findall("st.{2}ng",string)) # needs to have the '.'
    print(re.findall("st{2}ng",string))


    # "|" - Exactly the specified number of occurrences
    # tried from left to right
    print("\n"+"Using '|'".center(print_str_length1,"-"))
    s = "This is a baby right? or is it an adult?. I think it's a baby boy"
    print(re.findall("baby|adult",s))

def regex_specialSequence():
    '''All the special sequences of regular expressions are used here'''
    
    print("\n"+" Special Sequences ".center(print_str_length2,"-"))


    print("Using '\\A' (beginning of string)".center(print_str_length1,"-"))
    # \A = Returns a match where the specified characters are at
    # the beginning of a word
    print(re.findall(r"\AThis", string))
    print(re.findall(r"\AHello", string)) # nothing found


    print("Using '\\Z' (end of string)".center(print_str_length1,"-"))
    # \Z = Returns a match where the specified characters are at
    # the end of a word
    print(re.findall(r"string\Z", string)) # nothing found
    print(re.findall(r"com\Z", string)) 


    print("\n"+"Using '\\b' (beginning/end of any word)".center(print_str_length1,"-"))
    # \b = Returns a match if the specified characters
    # are at the beginning or end of any word in the string
    print(re.findall(r"\btest", string)) # beginning of the word
    print(re.findall(r"llo\b", string)) # end of the word


    print("\n"+"Using '\\B' (Not beginning/end of any word)".center(print_str_length1,"-"))
    # \B = Returns a match if the specified characters
    # are at any other position than the beginning/end
    # of the word in the string
    print(re.findall(r"\Beste", string)) # not beginning/end of the word
    print(re.findall(r"ell\B", string)) # not beginning/end of the word
    print(re.findall(r"\BThis", string)) # Start of word


    print("\n"+"Using '\\d' (string contains [0, 9])".center(print_str_length1,"-"))
    # \d = Returns a match where the string contains digits (numbers from 0-9)
    s = "10.10 abab 56@78 ghjk 99hh"
    print(re.findall(r"\d", s))


    print("\n"+"Using '\\D' (string does not contain contains [0, 9])".center(print_str_length1,"-"))
    # \D = Returns a match where the string does not contains digits (numbers from 0-9)
    print(re.findall(r"\D", s)) # also includes white spaces


    print("\n"+"Using '\\s' (string contains a white space and '\\n)'".center(print_str_length1,"-"))
    # \s = Returns a match where the string contains a white space character
    print(re.findall(r"\s", string)) 


    print("\n"+"Using '\\S' (string does not contain a white space and '\\n)'".center(print_str_length1,"-"))
    # \S = Returns a match where the string does notcontains a white space character
    print(re.findall(r"\S", string)) 


    print("\n"+"Using '\\w' (string contains [a-z][A-Z][0-9] and underscores)'".center(print_str_length1,"-"))
    # \w = Returns a match where the string does notcontains a white space character
    print(re.findall(r"\w", string)) 


    print("\n"+"Using '\\W' (string does not contain [a-z][A-Z][0-9] and underscores)'".center(print_str_length1,"-"))
    # \W = Returns a match where the string does notcontains a white space character
    print(re.findall(r"\W", string)) 

if __name__ == "__main__":
    regex_notes()
    regex_metaCharacters()
    regex_specialSequence()