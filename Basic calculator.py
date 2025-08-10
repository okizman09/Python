def basic_calc():
    print("This is basic calculator program  that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).\n Enter q to quit")
basic_calc()
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

while num1 or num2 != "q":
    try:
        num1 = float(num1)
        print(f"You entered: {num1}")
        break
    except ValueError:
        input("❌ That’s not a valid number. Try again: ")
    try:
        num2 = float(num2)
        input(f"You entered: {num2}")
        break
    except ValueError:
        input("❌ That’s not a valid number. Try again: ")

#num1 = int(input("Input first number: "))

#num2 = int(input("Input second number: "))
print("+ - * /")
operation = input("Select operation to be carried out: + - * / : ")
print("Input q to quit")
while operation != "q":
    if operation == "+":
        calc = num1 + num2
        print(f"Your answer is {calc}")
    elif operation == "-":
        calc = num1 - num2
        print(f"Your answer is {calc}")
    elif operation == "*":
        calc = num1 * num2
        print(f"Your answer is {calc}")
    elif operation == "/":
        calc = num1 / num2
        print(f"Your answer is {calc}")
    else:
        input("Incorrect input,\n input must be + - * / \n q to quit: ")

