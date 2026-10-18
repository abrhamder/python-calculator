number1 = float(input("Please input the number:-"))
operator = input("Please input the operator ")
number2 = float(input("Please input the number "))


if operator == "+":
    print("Result=", number1 + number2)
elif operator == "-":
    print("Result=", number1 - number2)
elif operator == "*":
    print("Result=", number1 * number2)
elif operator == "/":
    if number2 != 0:
        print("Result=", number1 / number2)
    else:
        print("cannot devided by 0!")
else:
    print("Invalid Request!")
     



