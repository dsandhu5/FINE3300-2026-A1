import csv


class ExchangeRates:
    def __init__(self, filename):
        with open(filename, newline="", encoding="utf-8-sig") as file:
            rows = list(csv.DictReader(file))

        if not rows:
            raise ValueError("The exchange rate file contains no data.")

        # Read the latest rate from the last row.
        latest_row = rows[-1]
        self.date = latest_row["Date"]
        self.rate = float(latest_row["FXAUSDCAD"])

        if self.rate <= 0:
            raise ValueError("The USD/CAD exchange rate must be positive.")

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        if from_currency not in ("USD", "CAD") or to_currency not in ("USD", "CAD"):
            raise ValueError("Currencies must be USD or CAD.")

        if from_currency == to_currency:
            return amount
        elif from_currency == "USD":
            return amount * self.rate
        else:
            return amount / self.rate


if __name__ == "__main__":
    try:
        exchange_rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

        amount = float(input("Enter the amount to convert: "))
        from_currency = input("From currency (USD or CAD): ").strip().upper()
        to_currency = input("To currency (USD or CAD): ").strip().upper()

        result = exchange_rates.convert(amount, from_currency, to_currency)

        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        print(f"Exchange rate date: {exchange_rates.date}")

    except (OSError, ValueError) as error:
        print(f"Error: {error}")