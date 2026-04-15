print("Welcome to currency converter")
print("Supported currencies: USD, INR, EUR, GBP, JPY, AED")
cur= ["USD",'INR','EUR','GBP','JPY','AED']
rates= {
    'USD': 1.0,
    'INR':83.0,
    'EUR': 0.92,
    'GBP': 0.78,
    'JPY': 141.0,
    'AED': 3.67,
}
def convert():
                user_amount = float(input("Enter the amount to be converted: "))
            # Convert to USD first
                amount_in_usd = user_amount / rates[source_cur]
            # Then convert USD to target currency
                converted_amount = amount_in_usd * rates[target_cur]
                print(f"Your amount in {target_cur.upper()} is {round(converted_amount, 2)}")
while True:
    source_cur = input("\nEnter your source currency code: ").upper()
    target_cur = input("Enter the target currency code: ").upper()
    
    if source_cur in cur and target_cur in cur:
        try:
           convert()
        except ValueError:
            print("Invalid number! Please enter a numeric amount.")
    else:
        print("Invalid currency code entered. Please enter a valid one.")

    continue_or_not = input("Do you want to convert again? (y/n): ").lower()
    if continue_or_not != 'y':
        break
print("Thank you for using the converter!")
            



