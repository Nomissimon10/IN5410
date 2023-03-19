import numpy as np

# Installed mathplot with "pip3 install matplotlib"
import matplotlib.pyplot as plt


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


def plotHourlyConsumption(schedule, appliances):
    # Example data
    categories = list(range(24))
    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
              '#800000', '#008000', '#000080', '#808000', '#800080', '#008080',
              '#FFA500', '#FFC0CB', '#FFD700', '#FFE4B5', '#7FFFD4', '#DA70D6',
              '#00BFFF', '#9400D3']

    # Set up the positions and width for the bars
    r = np.arange(len(categories))

    # Plot the bars
    total = [0] * 24
    index = 0
    for appliance in appliances:
        arr = [0] * 24
        for i in range(24):
            hour = schedule[i]
            if appliance in hour:
                hourly_consumption = round(
                    (appliance.consumption / appliance.duration) / 1000, 2)
                for j in range(appliance.duration):
                    arr[(i + j) % 24] = hourly_consumption
                    total[(i + j) % 24] += hourly_consumption
                break

        print(f"{appliance.name} - {arr}")
        plt.bar(r, arr, color=colors[index], label=appliance.name)
        index += 1
    print(total, sum(total))

    # Add xticks on the middle of the group bars
    plt.xlabel('Categories')
    plt.xticks(r, categories)
    plt.ylabel('Consumption (kWh)')

    # Add a legend
    plt.legend()

    # Show the chart
    plt.show()
