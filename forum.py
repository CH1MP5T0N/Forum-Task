import math
while True:
    numerator = eval(input("Enter a Numerator, Value must be greater than 0: "))
    while numerator < 0:
        numerator = eval(input("Please re-enter a Numerator, Value must be greater than 0: "))
    denominator = eval(input("Enter a Denominator, Value must be greater than 0: "))
    while denominator < 0:
        denominator = eval(input("Please re-enter a Denominator, Value must be greater than 0: "))
    gcd = math.gcd(numerator, denominator)
    gcdn = numerator//gcd; gcdd = denominator//gcd; whole = numerator//denominator
    if denominator > numerator:
        print(f"{numerator}/{denominator} is a proper fraction.")
        if gcd == 1:
            print("This proper fraction cannot be reduced any further.")
        else:
            print(f"The proper fraction can be reduced further to become: {gcdn}/{gcdd}")
    else:
        gcc = math.gcd(gcdn,gcdd)
        print(f"{numerator}/{denominator} is an improper fraction.")
        if gcd == 1 and denominator > 1:
            print(f"The improper fraction cannot be reduced any further.\nThe mixed number is {whole} and {gcdn-(whole*gcdd)}/{gcdd}")
        elif gcd == 1:
            print(f"The improper fraction cannot be reduced any further.\nThe whole number is {whole}")
        elif gcc ==1 and gcdd > 1:
            print(f"The improper fraction can be reduced further to become: {gcdn}/{gcdd}\nThe mixed number is {whole} and {gcdn - (whole * gcdd)}/{gcdd}")
        else:
            print(f"The improper fraction can be reduced further to become: {gcdn}/{gcdd}\nThe whole number is {whole}")
    end = (input("Do you want to do another fraction (y/n): "))
    if end == "y":
        continue
    elif end == "n":
        break
    else:
        print("Ill take that as a no\nEnding program...")
        break