import math
from generateElectricityPrices import generate_electricity_prices
from classes import Appliance, createAppliances


prices = generate_electricity_prices()

print(prices)


def estimate_electricity_cost_for_run(hour: int, duration, consumes: int) -> int:
    global prices
    consumes = consumes / 1000
    cost = 0
    for i in range(hour, hour + math.ceil(duration)):
        if i >= 24:
            i -= 24
        cost += prices[i] * (consumes)
    # If duration is not a whole number, removes the decimal from the last hour
    if isinstance(duration, float):
        last_hour = hour + math.ceil(duration)
        # If duration is 1.8, 0.2 would have to be removed (decimal)
        decimal = (math.ceil(duration) - duration)
        if last_hour >= 24:
            last_hour -= 24
        if prices[hour] < prices[last_hour]:
            cost -= (prices[last_hour] * consumes) * decimal
        else:
            cost -= (prices[last_hour] * consumes) * decimal
        return cost

# * DESCRIPTION: Estimates the electricity cost for a given hour
# * INPUT: hours: int, min: int, max: int
# * OUTPUT: int


def estimate_best_hour_start(duration: float, min_hour: int, max_hour: int, consumes: int) -> int:
    global prices
    min_cost = -1
    min_index = -1
    if max_hour < min_hour:
        max_hour += 24
    for hour in range(min_hour, max_hour - math.ceil(duration)):
        if hour >= 24:
            hour -= 24
        cost = estimate_electricity_cost_for_run(hour, duration, consumes)
        if cost < min_cost or min_cost == -1:
            min_cost = cost
            min_index = hour

    return min_index

# * DESCRIPTION: Calculates the optimal schedule for the given appliances
# * INPUT: appliances: Appliance[] -> list of appliances
# * OUTPUT: dict -> {hour: Appliance[]}


def optimal_calculation(appliances):
    schedule = {}
    for i in range(24):
        schedule[i] = []

    # * Calculate optimal schedule
    for appliance in appliances:
        hour_start = estimate_best_hour_start(
            appliance.duration, appliance.timeStart, appliance.timeStop, appliance.consumption)
        print("Hour start", hour_start)
        print(f'{appliance.name} -> {hour_start} - {hour_start + appliance.duration}')
        schedule[hour_start].append(appliance)

    return schedule

# * DESCRIPTION: Calculates the total daily energy consumption for the given schedule
# * INPUT: schedule: dict -> {hour: Appliance[]}
# * OUTPUT: int


def calculate_schedule_cost(schedule: dict) -> int:
    total = 0
    for hour in schedule:
        for appliance in schedule[hour]:
            total += estimate_electricity_cost_for_run(
                hour, appliance.duration, appliance.consumes)

    return int(total)


#schedule = optimal_calculation(createAppliances()[0])
# print(schedule)
#print(f'{calculate_schedule_cost(schedule)}nok for this schedule')
