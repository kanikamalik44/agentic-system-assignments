x = input("Enter first number")
y = input("Enter second number")
try:
    if type(int(x)) == int and type(int(y)) == int :
        if int(y) == 0:
            print("Cannot divide by zero")
        else:
             print(f"Their sum is {int(x)+int(y)}")
             print(f"Their division result is {int(x)/int(y)}")       
except ValueError:
    print("Invalid input")