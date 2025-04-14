import requests


def get_exchange_rate(source_currency, target_currency, api_key):
    # URL for ExchangeRate-API (you can modify this URL based on the API you're using)
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}"

    # Send GET request to the API
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            # Fetch the exchange rate for the target currency
            exchange_rate = data['conversion_rates'].get(target_currency)
            if exchange_rate:
                return exchange_rate
            else:
                print("Error: Invalid target currency code.")
                return None
        else:
            print("Error: Could not fetch exchange rates.")
            return None
    else:
        print("Error: Unable to connect to the API.")
        return None


def convert_currency(amount, exchange_rate):
    # Convert the amount using the exchange rate
    return amount * exchange_rate


# Main function
if __name__ == "__main__":
    # Your API Key from ExchangeRate-API
    api_key = "YOUR_API_KEY"  # Replace this with your actual API key

    # Take user input for amount, source currency, and target currency
    amount = float(input("Enter amount: "))
    source_currency = input("Convert from (e.g., USD): ").upper()
    target_currency = input("Convert to (e.g., INR): ").upper()

    # Get the exchange rate from the API
    exchange_rate = get_exchange_rate(source_currency, target_currency, api_key)

    if exchange_rate:
        # Convert the amount
        converted_amount = convert_currency(amount, exchange_rate)
        # Display the result
        print(f"Converted Amount: {converted_amount:.2f} {target_currency}")
