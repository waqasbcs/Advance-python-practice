# First, install pycountry if you haven't already
# pip install pycountry

import pycountry

def get_currency(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        currency = pycountry.currencies.get(numeric=country.numeric)
        return f"The currency of {country_name} is {currency.name}"
    except Exception:
        return "Country not found or currency information unavailable."

# Input country name
country_name = input("Enter Country Name: ")
print(get_currency(country_name))


