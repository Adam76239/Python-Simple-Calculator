

def add(num1, num2):
    answer = int(num1) + int(num2)
    return answer
    
def sub(num1, num2):
    answer = int(num1) - int(num2)
    return answer

def mul(num1, num2):
    answer = int(num1) * int(num2)
    return answer

def div(num1, num2):
    answer = int(num1) / int(num2)
    return answer    


print("This is the Python Simple Calculator",
    "\nIt can add, subtract, multiply and divide.",
    "\nPlease enter:", "\n1 to add", "\n2 to subtract",
    "\n3 to multiply", "\n4 to divide")

choice = input(">")
num1 = input("first number?")
num2 = input("second number?")


if choice == "1":
    add (num1, num2)
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    sub(num1, num2)
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == "3":
    sub(num1, num2)
    print(num1, "*", num2, "=", mul(num1, num2))

elif choice == "4":
    sub(num1, num2)
    print(num1, "/", num2, "=", div(num1, num2))

else:
    print("I'm sorry, you did not choose an operation.", "\nPlease try again.")
    