'''import random
num1= input("enter user number")
num2= random.randint(1,100)

if num1 >= num2:
    print("user number is greater")

else:
    print("user number smaller")'''

def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def count_frequency(items):
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


numbers = [12, 45, 23, 12, 67, 34, 45, 89, 23, 12]

total, average, maximum, minimum = calculate_statistics(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", round(average, 2))
print("Maximum:", maximum)
print("Minimum:", minimum)

print("\nFrequency:")
for number, count in count_frequency(numbers).items():
    print(number, "->", count)


names = ["Aanya", "jade", "max", "sean", "oliver"]

print("\nStudents:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")


