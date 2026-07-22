import math

print("=" * 40)
print("        NUMBER ANALYZER")
print("=" * 40)

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

# Display Results
print("\n" + "=" * 40)
print("Analysis Result")
print("=" * 40)

for item in properties:
    print("✔", item)

print("=" * 40)