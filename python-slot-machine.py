import random

MAX_LINES =3
MAX_BET= 1000
MIN_BET= 10
ROWS= 3
COL= 3

'''slot = [
    ["🍒", "⭐", "💎"],
    ["⭐", "🍒", "🍒"],
    ["💎", "⭐", "🍒"]
]'''
symbol_values = {
    "🍒": 2,
    "⭐": 4,
    "💎": 3
}
'''for row in slot:
    print(" | ".join(row))'''

def get_slot_machine_symbols(rows,col,symbols):
     all_symbols=[]
     for symbol, symbol_values in symbols.items():
         for _ in range(symbol_values):
             all_symbols.append(symbol)

     columns= []
     for _ in range(col):
         column=[]
         current_symbols= all_symbols[:]
         for _ in range(rows):
             value= random.choice(current_symbols)
             current_symbols.remove(value)
             column.append(value)

         columns.append(column)

     return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")

            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount= input("Enter the amount you want to deposit ($): ")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount 

def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines you want to bet on (1-"+ str(MAX_LINES)+"): ")

        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines 

def get_bet():
    while True:
        amount= input("Enter the amount you want to bet on each line($): ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")

    return amount 

def check_winnings(columns, lines, bet, values):
    winnings = 0

    for line in range(lines):
        symbol = columns[0][line]  # first symbol of that row

        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet

    return winnings
def chance_s(balance):
    lines= get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet*lines

        if total_bet > balance:
            print(f"You do not have enough balance, ypur current balance is ${balance}")

        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is equal to ${total_bet}.")
    
    slots= get_slot_machine_symbols(ROWS, COL,symbol_values)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")

    balance += winnings - total_bet
    print(f"New balance: ${balance}")

    return balance

    
    

def main():
    balance= deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin= input("Press enter to spin ('n' to quit)")
        if spin.lower() == "n":
            break
        balance = chance_s(balance)

    print(f"You left with ${balance}")

main()