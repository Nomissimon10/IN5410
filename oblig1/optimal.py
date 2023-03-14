import math
from classes import Appliance

prices = {
    0: 0.17043824334020852,
    1: 0.17687964847282173,
    2: 0.1848716150231699,
    3: 0.16119955296182936,
    4: 0.16220396601978404,
    5: 0.17861609773844922,
    6: 0.19649085997831328,
    7: 0.36008332379269636,
    8: 0.396606737372287,
    9: 0.5501378614431885,
    10: 0.5940889787258893,
    11: 0.18848951740313521,
    12: 0.18571010112349637,
    13: 0.16788191713340134,
    14: 0.1709039894099174,
    15: 0.16532830213734045,
    16: 0.4565517132282808,
    17: 0.5857373298786244,
    18: 0.3656057042514985,
    19: 0.49303826836168463,
    20: 0.38306623023534225,
    21: 0.43242741485567326,
    22: 0.1580491724358629,
    23: 0.17048220206057746
}


def estimate_electricity_cost_for_run(hour: int, duration: int, consumes: int) -> int:
    global prices

    cost = 0
    for i in range(hour, hour + duration):
        if i >= 24:
            i -= 24
        cost += prices[i] * (consumes / duration)

    return cost

# * DESCRIPTION: Estimates the electricity cost for a given hour
# * INPUT: hours: int, min: int, max: int
# * OUTPUT: int


def estimate_best_hour_start(duration: int, min_hour: int, max_hour: int, consumes: int) -> int:
    global prices

    min_cost = -1
    min_index = -1
    if max_hour < min_hour:
        max_hour += 24
    for hour in range(min_hour, max_hour - duration):
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
        if not appliance.shiftable or ((appliance.timeStart + appliance.duration) % 24) == appliance.timeStop % 24:
            schedule[appliance.timeStart].append(appliance)
            continue

        hour_start = estimate_best_hour_start(
            appliance.duration, appliance.timeStart, appliance.timeStop, appliance.consumption)
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
                hour, appliance.duration, appliance.consumption)

    return round(total / 1000, 2)


def print_schedule(schedule: dict) -> None:
    for hour in schedule.keys():
        if (len(schedule[hour]) == 0):
            continue
        for appliance in schedule[hour]:
            print(
                f'{f"{hour}:00-{hour + appliance.duration}:00":<11} - {appliance.name:<16} ({appliance.consumption / 1000} kW)')