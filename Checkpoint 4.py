def calculator(num1, num2):
    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Cannot divide by zero!"
            else:
                return num1 / num2
        else:
            return "Invalid operator!"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(num1, num2)

print("The result is:", result)
