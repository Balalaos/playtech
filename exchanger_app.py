from convetor import Currency_Convertor
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
  
app.secret_key = 'app'


@app.route('/')
#Main page where user can enter money amount and currencies
@app.route('/main', methods =['GET', 'POST'])
def main():
    message = ''
    if request.method == 'POST' and 'first_currency' in request.form and 'second_currency' in request.form and 'amount' in request.form:
        from_currency = request.form['first_currency']
        to_currency = request.form['second_currency']
        amount = request.form['amount']
        
        # Check if currencies entered correctly
        if from_currency not in currencies or to_currency not in currencies:
            return render_template('main.html', message  = "Wrong currencies")
        if from_currency == to_currency:
            return render_template('main.html', message  = "Please use different currencies")
        
        # Check if amount entered correctly
        try:
            amount = float(amount)
        except ValueError:
            return render_template('main.html', message  = "Please use numbers for amount")
        if amount > 10000000000:
            return render_template('main.html', message  = "Number is too big! Maximum is 10000000000")

        # Convert all currencies and find profit for company
        from_intermediaries_rates, to_intermediaries_rates, maximus, profit = convertor.convert_currency(amount, from_currency, to_currency)
        # Prepare data for showing on the screen
        session["from_intermediaries_rates"] = from_intermediaries_rates
        session["to_intermediaries_rates"] = to_intermediaries_rates
        session["maximus"] = maximus
        session["profit"] = profit
        session["From_currency"] = from_currency
        session["To_currency"] = to_currency
        session["amount"] = amount
        return render_template('show_loans.html', message = message )
    return render_template('main.html', message  = message )


#This page show borrower data after search request or register a new loan
@app.route('/show_loans')
def show_loans():
    #Delete all data
    session.pop('from_intermediaries_rates', None)
    session.pop('to_intermediaries_rates', None)
    session.pop('maximus', None)
    session.pop('profit', None)
    session.pop('From_currency', None)
    session.pop('To_currency', None)
    session.pop('amount', None)
    return redirect(url_for('main'))


if __name__ == '__main__':
    #Activation of convertor class
    convertor = Currency_Convertor()
    #Available currrencies list
    currencies = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "HKD", "CNY", "SGD"]
    #Get current rates and caching them for future use
    convertor.get_currency_rates(currencies)
    app.run()