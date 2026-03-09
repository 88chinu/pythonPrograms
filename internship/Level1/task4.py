#Calculator program

def calculator(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Division by zero not allowed"
        case "%":
            return a % b
        case _:
            return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

result = calculator(num1, num2, operator)

print("Result:", result)