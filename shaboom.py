num1=float(input("First no.?"))
num2=float(input("Second no.?"))
operations = input("choose operation('+','-','/','*')")

if operations == '+':
    result = num1 + num2
    print(f"{num1}+{num2}=", result)

if operations == '-':
    result = num1 - num2
    print(f"{num1}-{num2}=", result)

if operations == '/':
    result = num1 / num2
    print(f"{num1}/{num2}=", result)

if operations == '*':
    result = num1 * num2
    print(f"{num1}*{num2}=", result)

    
