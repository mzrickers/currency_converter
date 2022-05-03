from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "adabd5ff5f2b5b5b0338"

printer = PrettyPrinter()

def get_currencies():
  endpoint = f"api/v7/currencies?apiKey={API_KEY}"
  url = BASE_URL + endpoint
  data = get(url).json()['results']

  data = list(data.items())
  data.sort()

  return data

def print_currencies(currencies):
  for name, currency in currencies:
    name = currency['currencyName']
    _id = currency['id']
    symbol = currency.get("currencySymbol", "")
    print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
  endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
  url = BASE_URL + endpoint
  response = get(url)

  data = response.json()

  printer.pprint(data)

# data = get_currencies()

# print_currencies(data)

exchange_rate("USD", "CZK")