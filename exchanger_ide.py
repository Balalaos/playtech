from convetor import Currency_Convertor


# This function printing all data for user
# This function is used only in version without GUI
def print_table(from_intermediaries, to_intermediaries, maximus, profit, from_currency, to_currency, amount):
        print()
        print(f"Conversion " + str(amount) + " " + from_currency + " to " + to_currency + ":")
        print("{:<10} {:<20} {:<25} {:<20}".format("Currency", "to intermediary","from intermediary", "Profit"))
        for currency, rate in from_intermediaries.items():
            print("{:<10} {:<20} {:<25} {:<20}".format(currency, round(to_intermediaries[currency],4), rate, profit[currency]))
        print()
        print("Our profit: {} by using {} as intermediary currency".format(maximus["max_profit"], maximus["max_profit_key"]))
        print("Best for user: {} intermediary currency, he will get {}".format(maximus["max_money_key"], maximus["max_money"]))


# Main function
if __name__ == '__main__':
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "HKD", "CNY", "SGD"]
    #Activation of convertor class
    convertor = Currency_Convertor()
    #Get current rates and caching them for future use
    convertor.get_currency_rates(currencies)
    
    while True:
        # Ask for currency types
        print("\nWe have this currencies: ", currencies)
        print("Write exit for exit or ")
        answer = input("Write from what currency to what currency you want to convert with space between: ")
        # Check if user wants to leave
        if answer == "exit":
            break
        
        # Check if currencies entered correctly
        try:
            from_currency, to_currency = answer.split()
        except ValueError:
            print("\nWrite currencies with space!!!")
            continue
        if from_currency not in currencies or to_currency not in currencies:
            print("\nWrong currencies!!!")
            continue
        if from_currency == to_currency:
            print("\nPlease use different currencies!!!")
            continue
        
        # Check if amount entered correctly
        try:
            amount = input("What amount you want to change?  ")
            amount = float(amount)
        except ValueError:
            print("\nPlease use numbers for amount!!!")
            continue
        if amount > 10000000000:
            print("\nNumber is too big!!! Maximum is 10000000000")
            continue
        
        #Convert currencies and print result
        from_intermediaries, to_intermediaries, maximus, profit = convertor.convert_currency(amount, from_currency, to_currency)
        print_table(from_intermediaries, to_intermediaries, maximus, profit, from_currency, to_currency, amount)