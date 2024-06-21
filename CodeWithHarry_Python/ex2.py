# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all
# the problems except : 45*3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and two numbers
# as input from the user and return the result.

print("--- Simple Calculator (Faulty) ---")

n1 = op = n2 = output = None

try:
    n1 = float(input("Enter 1st number : "))
except:
    print("Error in input")
    exit()

op = input("Enter the operator : ")

try:
    n2 = float(input("Enter 2nd number : "))
except:
    print("Error in input")
    exit()

    output = 1.1

if (op[0] == "+"):
    if(n1 == 56 and n2 == 9) or (n1 == 9 and n2 == 56):
        output = 77
    else:
        output = n1 + n2

elif (op[0] == "-"):
    output = n1 - n2

elif (op[0] == "*"):
    if(n1 == 45 and n2 == 3) or (n1 == 3 and n2 == 45):
        output = 555
    else:
        output = n1 * n2

elif (op[0] == "/"):
    if(n1 == 56 and n2 == 6) or (n1 == 6 and n2 == 56):
        output = 4
    else:
        output = n1 / n2

else:
    print("Please enter a valid operator next time")

try:
    if op[1]:
        for i in ['/','*','+','-']:
            if i in op:
                print("[ERROR in operator] [operator set to - '"+ i +"']")
                op = i
                if op == "/":
                    output = n1 / n2
                if op == "*":
                    output = n1 * n2
                if op == "+":
                    output = n1 + n2
                if op == "-":
                    output = n1 - n2
                break
except:
    pass
print(n1, op[0], n2, "=", round(output,3))