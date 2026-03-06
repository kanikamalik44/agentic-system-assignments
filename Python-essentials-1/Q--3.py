n = input("Enter name ")
a = input("Enter your age ")

try:
    if int(a) >= 0:
        print(f"Hello {n}")
        if int(a) < 13:
            print("You are a Child")
            print("You are not eligible to vote")
        elif (13 <= int(a) <= 17) :
            print("You are a Teenager")
            print("You are not eligible to vote")
        elif (18 <= int(a) <= 59) :
            print("You are an Adult")
            print("You are eligible to vote")
        elif (60 <= int(a)) :
            print("You are a Senior Citizen")
            print ("You are eligible to vote")
    else:
        print("Age cannot be negative")
except ValueError:
    print("Invalid age input")