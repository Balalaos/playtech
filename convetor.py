import requests
import json
import math
#saved in the file currency rates for debugging purpuses
from debug_data import rates_dict

#This class:
# downloading rates
# caching them
# converting currencies from one to another
# searching best ones for costumer and server
# showing them on the screen
class Currency_Convertor():
    def __init__(self):
        #rates cahce
        self.cache_rates = {}
        pass
    
    
    #This function is downloading rates and cahcing them.
    # It activates one time during a start of program and download all needed rates for used currencies
    def get_currency_rates(self, currencies):
        #link for API
        url = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"
        #all needed headers
        headers = {
            "X-RapidAPI-Key": "aa2609059fmsh3ac73fe37daef73p11fba6jsn9fc38bd73188",
            "X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com"
        }

        #Loop downloading rates for every currencies
        for currency in currencies:
            #Change left currencies from array to string for sending message
            intermediaries = [c for c in currencies if c not in [currency]]
            intermediaries = ', '.join(intermediaries)
            #message with reques fom API
            querystring = {"base":currency,"symbols":intermediaries}
            
            #True - use saved in the file currency rates
            #False - Use currency from API
            #Most of API hve limit for use. That is made for saving limit for latest tests
            debug = False
            if debug:
                data = rates_dict[currency]
            else:
                #get all rates for current currency
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = json.loads(response.text)
                data = data["rates"]
                
            #save data in cache
            self.cache_rates[currency] = data
        
       
    #This function get rates of 2 named by user currencies from cache 
    def get_rates_for_currency(self, From_currency, To_currency):
        # coppies rates from first currency to intermidiary currency
        to_intermediaries_rates = {}
        to_intermediaries_rates.update(self.cache_rates[From_currency])
        # deleting the second currency from dictonary
        del to_intermediaries_rates[To_currency]
        
        # coppies rates from intermidiary currency to second currency
        # as money should be converted to second currency from intermidiary, this loop searching 
        # all rates from intermidiary currency to second currency
        from_intermediaries_rates = {}
        for currency in self.cache_rates:
            for item in self.cache_rates[currency]:
                if item == To_currency and currency != From_currency:
                    from_intermediaries_rates[currency] = self.cache_rates[currency][item]
        return to_intermediaries_rates, from_intermediaries_rates



    # This function convert entered by user amount from one currency to another
    def convert_currency(self, amount, From_currency, To_currency):
        # Getting rates for converting from first currency to intermidiary currency and from intermidiary currency to final one
        to_intermediaries, from_intermediaries = self.get_rates_for_currency(From_currency, To_currency)
        to_intermediaries = dict(sorted(to_intermediaries.items()))
        from_intermediaries = dict(sorted(from_intermediaries.items()))
        
        profit = {}
        max_money = 0
        max_money_key = []
        max_profit = 0
        max_profit_key = []
        # This loop is making converting to intermidiary currency and the final one
        # and finding the best options for user and service
        for currency in to_intermediaries:
            # converting to intermidiary currency 
            to_intermediaries[currency] = amount * to_intermediaries[currency]
            # converting to the final currency
            num = from_intermediaries[currency] * to_intermediaries[currency]
            
            # searching the best options for user
            if num > max_money:
                max_money = num
                max_money_key = []
                max_money_key.append(currency)
            elif num == max_money:
                max_money_key.append(currency)
            
            #round numbers
            num = round(num, 4)
            from_intermediaries[currency] = num
            to_intermediaries[currency] = round(to_intermediaries[currency], 4)

            # counting fractions of cents
            rounded_num = math.floor(num * 100)/100.0
            decimal_num =  round(num - rounded_num, 4)
            profit[currency] = decimal_num
            
            # searching the best options for service
            if decimal_num > max_profit:
                max_profit = decimal_num
                max_profit_key = []
                max_profit_key.append(currency)
            elif decimal_num == max_profit:
                max_profit_key.append(currency)
        
        max_money_key = ', '.join(max_money_key)
        max_profit_key = ', '.join(max_profit_key)
        # Creating directory with all best options for user and service
        maximus = {"max_money": max_money, "max_money_key":max_money_key, "max_profit":max_profit, "max_profit_key":max_profit_key}
        # Returning all converted money to to intermediaries currencies, to the final currency, 
        # best options and profit for intermediaries currencies 
        return from_intermediaries, to_intermediaries, maximus, profit

