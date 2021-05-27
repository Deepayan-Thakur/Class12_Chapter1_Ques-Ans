# to find that is it a 1/2/3 digit number using a nested if statements ?

n = int(input("Enter a number between (0 to 999) only : "))

if n >= 0 and n < 10:
    print(n, "is a 1 digit number...") 

else:
    if n >= 10 and n < 100:
        print(n,"is a 2 digit number...")

    else:
        if n >= 100 and n < 1000:
            print(n,"is a 3 digit number...")

        else:
            print("\nInvalid entry...\nPlease enter from (0 to 999) only\n")
