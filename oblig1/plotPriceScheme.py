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


def plotHouseholdUsages(schedules):
    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
              '#800000', '#008000', '#000080', '#808000', '#800080', '#008080',
              '#FFA500', '#FFC0CB', '#FFD700', '#FFE4B5', '#7FFFD4', '#DA70D6',
              '#00BFFF', '#9400D3', '#FF0000', '#00FF00', '#0000FF', '#FFFF00',
              '#FF00FF', '#00FFFF', '#800000', '#008000', '#000080', '#808000',
              '#800080', '#008080', '#FFA500', '#FFC0CB', '#FFD700', '#FFE4B5',
              '#7FFFD4', '#DA70D6', '#00BFFF', '#9400D3']
    categories = []
    for i in range(len(schedules)):
        categories.append("Household " + str(i + 1))

    # Set up the positions and width for the bars
    r = np.arange(24)

    # Plot the bars
    index = 0
    total = [0] * 24
    for schedule in schedules:
        before = total.copy()
        data = [0] * 24
        for hour in range(24):
            hour_data = schedule[hour]
            for appliance in hour_data:
                hourly_consumption = round(
                    (appliance.consumption / appliance.duration) / 1000, 2)
                for i in range(appliance.duration):
                    data[(hour + i) % 24] += hourly_consumption
                    total[(hour + i) % 24] += hourly_consumption

        plt.bar(r, data, color=colors[index],
                label=categories[i], bottom=before)
        index += 1

    # Add xticks on the middle of the group bars
    plt.xlabel('Households')
    plt.xticks(r, r)
    plt.ylabel('Consumption (kWh)')

    # Add a legend
    plt.legend()

    # Show the chart
    plt.show()


def plotHourlyConsumptionForHousehold(schedule, appliances):
    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
              '#800000', '#008000', '#000080', '#808000', '#800080', '#008080',
              '#FFA500', '#FFC0CB', '#FFD700', '#FFE4B5', '#7FFFD4', '#DA70D6',
              '#00BFFF', '#9400D3']
    categories = list(range(24))

    # Set up the positions and width for the bars
    r = np.arange(len(categories))

    # Plot the bars
    total = [0] * 24
    index = 0
    for appliance in appliances:
        arr = [0] * 24
        before = total.copy()
        for i in range(24):
            hour = schedule[i]
            if appliance in hour:
                hourly_consumption = round(
                    (appliance.consumption / appliance.duration) / 1000, 2)
                for j in range(appliance.duration):
                    arr[(i + j) % 24] = hourly_consumption
                    total[(i + j) % 24] += hourly_consumption
                break

        plt.bar(r, arr, color=colors[index],
                label=appliance.name, bottom=before)
        index += 1

    # Add xticks on the middle of the group bars
    plt.xlabel('Categories')
    plt.xticks(r, categories)
    plt.ylabel('Consumption (kWh)')

    # Add a legend
    plt.legend()

    # Show the chart
    plt.show()
