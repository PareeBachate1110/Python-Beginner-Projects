#Exercise 7: Calculator

while True:
    a = float(input("Enter Number 1 : "))
    b = float(input("Enter Number 2 : "))

    op = input("Select Operation Which You Want To Perform (+,-,*,/): ")

    if op == "+":
        print(f"Addition of a and b : {round(a+b,2)}")
    elif op == "-":
        print(f"Subtraction of a and b : {round(a-b,2)}")
    elif op == "*":
        print(f"Multiplication of a and b : {round(a*b,2)}")
    elif op == "/":
        print(f"Division of a and b : {round(a/b,2)}")
    else:
        print("Error: Please Enter ONE of the Following : +, -, *, /")

    print("----------------------------------------------")
    