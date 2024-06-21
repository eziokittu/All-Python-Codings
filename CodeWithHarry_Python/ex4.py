# Pattern printing
try:
    n = int(input("Enter the number of rows (Positive Integer Only) : "))
    reverse = input("Enter 0 for Base on TOP, 1 for Base on BOTTOM : ")

    for i in range(0,n):
        if int(reverse):
            for j in range(0, i+1):
                print("*", end="")
        else:
            for j in range(0, n-i):
                print("*", end="")
        print("\r")
except:
    print("Invalid Input")