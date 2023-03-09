import numpy as np

# Installed mathplot with "pip3 install matplotlib"
import matplotlib.pyplot as plt
from generateElectricityPrices import generate_electricity_prices


def plotTable(pricesDict):
    # Generate prices
    prices = pricesDict

    # Extract values from price-dict to arra
    values = []
    for key in prices:
        values.append(prices[key])

    # Plot table
    x = np.arange(0, 24, 1)
    y = np.arange(0, 0.7, 0.05)
    plt.plot(values)
    plt.xticks(x)
    plt.yticks(y)
    plt.ylabel("Energy price")
    plt.xlabel("Timeslot")
    plt.show()
