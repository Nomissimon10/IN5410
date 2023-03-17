import random


def generate_electricity_prices():
    # Define the base price for electricity
    base_price = 0.10

    # Define the peak hours and off-peak hours
    peak_hours = [16, 17, 18, 19, 20]
    off_peak_hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 21, 22, 23]

    # Create a dictionary to store the prices for each hour
    prices = {}

    # Loop through each hour of the day
    for hour in range(24):
        # Define the peak price and off-peak price
        peak_price = random.uniform(0.10, 0.50)
        off_peak_price = random.uniform(0.05, 0.10)
        # Determine if the hour is a peak hour or off-peak hour
        if hour in peak_hours:
            price = base_price + peak_price
        elif hour in off_peak_hours:
            price = base_price + off_peak_price
        else:
            price = base_price

        # Add the price to the dictionary
        prices[hour] = price

    # Return the dictionary of prices
    return prices
