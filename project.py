num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number"))
operation = input("Enter operation (+,-,*,/) ")

#Performing arithematic operations using elif
if operation == "+":
    result = num1 + num2
    print("addition:",result)
elif operation == "-":
    result = num1 - num2
    print("substraction:",result)
elif operation == "*":
    result = num1 * num2
    print("multiply",result)
elif operation == "/":
    result = num1 / num2
    print("division=",result)
else:
     result = "Invalid operation!"
     print("Result:",result)