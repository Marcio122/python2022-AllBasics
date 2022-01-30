num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter Operator: ")


if operator == '+':
    sum1 = (num1 + num2)
    print(f"The Addition Of {num1} And {num2} Results In: {sum1}")

elif operator == '-':
    sub1 = (num1 - num2)
    print(f"The Subtraction Of {num1} And {num2} Results In: {sub1}")


elif operator == '*':
    multi1 = (num1 * num2)
    print(f"The Product Of {num1} And {num2} Results In: {multi1}")

elif operator == '/':
    div1 = (num1 // num2)
    print(f"The Division Of {num1} And {num2} Results In: {div1}")
else:
    print("Invalid operator")