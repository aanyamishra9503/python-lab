import math
print("Welcome to the Number Analyser!")
print("This program will analyze the properties of a given number.")

num = int(input("Enter a number: "))

properties = []

# Positive / Negative / Zero
if num > 0:
    properties.append("Positive")
elif num < 0:
    properties.append("Negative")
else:
    properties.append("Zero")

# Even or Odd
if num % 2 == 0:
    properties.append("Even")
else:
    properties.append("Odd")

# Prime Check
if num > 1:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        properties.append("Prime")
    else:
        properties.append("Composite")
elif num == 1:
    properties.append("Neither Prime nor Composite")

# Perfect Square
if num >= 0:
    root = int(math.sqrt(num))
    if root * root == num:
        properties.append("Perfect Square")

# Divisible by 5
if num % 5 == 0:
    properties.append("Divisible by 5")

# Divisible by 10
if num % 10 == 0:
    properties.append("Divisible by 10")

# Armstrong Number
temp = abs(num)
digits = len(str(temp))
total = 0

for digit in str(temp):
    total += int(digit) ** digits

if total == temp:
    properties.append("Armstrong Number")

# Palindrome Number
if str(abs(num)) == str(abs(num))[::-1]:
    properties.append("Palindrome Number")

def isPerfectSquare(x):
    s = int(x ** 0.5)
    return s * s == x

print("\n" + "=" * 40)
print("Analysis Result")
print("=" * 40)

for item in properties:
    print(item)

print("=" * 40)

print("\nWould you like to see any additional information?")

while True:
    print("""
1. Multiplication Table
2. Square, Cube & Square Root
3. Factors
4. Sum of Digits
5. Reverse Number
6. Exit
""")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print(f"\nMultiplication Table of {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    elif choice == "2":
        print(f"\nSquare : {num ** 2}")
        print(f"Cube   : {num ** 3}")

        if num >= 0:
            print(f"Square Root : {round(num ** 0.5, 2)}")
        else:
            print("Square Root : Not a real number")

    elif choice == "3":
        factors = []
        for i in range(1, abs(num) + 1):
            if num % i == 0:
                factors.append(i)
        print("Factors:", factors)

    elif choice == "4":
        digit_sum = 0

        for digit in str(abs(num)):
             digit_sum += int(digit)

        print("Sum of Digits:", digit_sum)

    elif choice == "5":
        reverse = str(abs(num))[::-1]
        if num < 0:
            print("Reverse:", "-" + reverse)
        else:
            print("Reverse:", reverse)

    elif choice == "6":
        print("\nThank you for using Number Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")


print("Thank you for using the Number Analyser!")