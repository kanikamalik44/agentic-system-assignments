x = input("Enter first name ")
y = input("Enter last name ")
a = input("Enter age ")

print(f"Full Name:{x+" "+y} ")
try:
    if int(a) >= 0:
        if type(int(a)) ==int:
            print(f"You will be {int(a)+1} next year")
    else:
        print("Age cannot be negative")
except ValueError:
    print("Invalid age input")
