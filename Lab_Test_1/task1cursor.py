def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """
    Convert an amount from one currency to another using exchange rates.

    :param amount: The amount of money to convert (float or int).
    :param from_currency: The currency code of the original currency (str).
    :param to_currency: The currency code to convert to (str).
    :param exchange_rates: A dict mapping currency codes to their rates relative to a base currency.
    :return: The converted amount (float).
    :raises: ValueError if either currency is not in exchange_rates.
    """
    if from_currency not in exchange_rates:
        raise ValueError(f"Unknown currency: {from_currency}")
    if to_currency not in exchange_rates:
        raise ValueError(f"Unknown currency: {to_currency}")

    # Convert amount to base currency, then to target currency
    base_amount = amount / exchange_rates[from_currency]
    converted_amount = base_amount * exchange_rates[to_currency]
    return converted_amount
