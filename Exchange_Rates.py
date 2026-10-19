class ExchangeRates:

    # open file and read the usd cad exchange rate
    def __init__(self, exchange_rates_file):
        
        self.exchange_rates_file = exchange_rates_file

        f = open(self.exchange_rates_file)
        last_line = f.readlines()[-1].split(",")
        self.usd_cad_rate = float(last_line[-2])
        f.close()

    # convert amount from one currency to another
    def convert(self, amount, from_currency, to_currency):
        amount = float(amount)

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD":
            return amount * self.usd_cad_rate
        else:
            return amount / self.usd_cad_rate

# prompt and read user input
amount = input("Amount: ")
from_currency = input("Convert from (USD or CAD): ")
to_currency = input("Convert to (USD or CAD): ")

# initialize converter and perform conversion
converter = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
result = converter.convert(amount, from_currency, to_currency)
print(result)
print(f"${result:,.2f} {to_currency}")