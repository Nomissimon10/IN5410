import math
from classes import Appliance
from appliances import nonShiftable, shiftable, auxilary

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


# * DESCRIPTION: Calculates total load for each hour based on all appliances, and peak hour + load
# * INPUT: appliances: Appliance[] -> list of appliances
# * OUTPUT: schedule: dict, peakHour: int, peakLoad: float

def calculate_peak_load(appliances):
    schedule = {}
    for i in range(24):
        schedule[i] = 0
    # Calculate total energy consumption for all appliances each hour
    for a in appliances:
        if not a.shiftable or ((a.timeStart + a.duration) % 24) == a.timeStop % 24:
            for i in range(24):
                schedule[i] += (a.consumption / 24)/1000
            continue
        hourStart = estimate_best_hour_start(
            a.duration, a.timeStart, a.timeStop, a.consumption
        )
        for i in range(hourStart, (hourStart + a.duration + 1)):
            schedule[i] += (a.consumption / a.duration)/1000
    # Find hour with highest energy consumption
    peakHour = 0
    peakPrice = schedule[peakHour]
    for hour in schedule.keys():
        if schedule[hour] > peakPrice:
            peakHour = hour
            peakPrice = schedule[peakHour]
    return schedule, peakHour, peakPrice


def scheduleAppliances(appliances):
    schedule = []
    for a in appliances:
        if not a.shiftable or ((a.timeStart + a.duration) % 24) == a.timeStop % 24:
            schedule.append({
                "name": a.name,
                "start": a.timeStart,
                "stop": a.timeStop,
                "duration": a.duration,
                "consumption": (a.consumption/a.duration)
            })
            continue
        optimalStartTime = estimate_best_hour_start(
            a.duration, a.timeStart, a.timeStop, a.consumption
        )
        schedule.append({
            "name": a.name,
            "start": optimalStartTime,
            "stop": a.timeStop,
            "duration": a.duration,
            "consumption": (a.consumption/a.duration)
        })
    # Sort schedule by appliance start time
    schedule = sorted(schedule, key=lambda x: x["start"])
    return schedule


def calculatePeak(schedule):
    hourlyTotalConsumption = {}
    totalCost = 0
    for i in range(24):
        hourlyTotalConsumption[i] = 0
    for appliance in schedule:
        for i in range(appliance["start"], (appliance["start"]+appliance["duration"])):
            hourlyTotalConsumption[i] += appliance["consumption"]/1000
    peakHour = 0
    peakLoad = hourlyTotalConsumption[peakHour]
    for hour in hourlyTotalConsumption:
        if hourlyTotalConsumption[hour] > peakLoad:
            peakHour = hour
            peakLoad = hourlyTotalConsumption[peakHour]
   # for hour in hourlyTotalConsumption:
    #    print(hour, " - ", hourlyTotalConsumption[hour])
    for x in schedule:
        totalCost += estimate_electricity_cost_for_run(
            x["start"], x["duration"], (x["consumption"]*x["duration"])/1000)

    return peakHour, peakLoad, totalCost


def applianceReference(appliance):
    for a in nonShiftable:
        if a == appliance["name"]:
            return nonShiftable[a]
    for a in shiftable:
        if a == appliance["name"]:
            return shiftable[a]
    for a in auxilary:
        if a == appliance["name"]:
            return auxilary[a]


def optimizeSchedule(schedule):
    # Create copy of schedule
    originalSchedule = schedule.copy()
    peakHour = calculatePeak(originalSchedule)[0]
    peakLoad = calculatePeak(originalSchedule)[1]
    totalCost = calculatePeak(originalSchedule)[2]
    lenght = len(originalSchedule)
    newSchedule = []
    print("Incomming:")
    print("Peak load", peakLoad)
    print("Total cost", totalCost)

    for i in range(len(originalSchedule)):
        if originalSchedule[i]["duration"] == 24:
            continue
        appliance = originalSchedule.pop(i)
        ref = applianceReference(appliance)
        for j in range(ref[4], ref[5]-ref[3]):
            originalSchedule.append({
                "name": appliance["name"],
                "start": j,
                "stop": ref[5],
                "duration": ref[3],
                "consumption": appliance["consumption"]
            })
            newPeakLoad = calculatePeak(originalSchedule)[1]
            newTotalCost = calculatePeak(originalSchedule)[2]
            if newPeakLoad > peakLoad and newTotalCost > totalCost:
                del originalSchedule[-1]
            elif newPeakLoad < peakLoad:  # her skal det egt stå newPeakLoad < peakLoad AND newTotalCost < total cost, men da kommer det ingen endringer
                peakLoad = newPeakLoad
                totalCost = newTotalCost
                appliance = originalSchedule.pop()
            else:
                del originalSchedule[-1]

        if len(originalSchedule) < lenght:
            originalSchedule.append(appliance)

    peakLoad = calculatePeak(originalSchedule)[1]
    totalCost = calculatePeak(originalSchedule)[2]
    print("Outgoing:")
    print("Peak load", peakLoad)
    print("Total cost", totalCost)

    return originalSchedule


# * DESCRIPTION: Calculates the total daily energy consumption for the given schedule
# * INPUT: schedule: dict -> {hour: Appliance[]}
# # * OUTPUT: int


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


def print_scedule_2(schedule):
    totalConsumption = 0
    totalCost = 0
    for x in schedule:
        totalConsumption += (x["consumption"]/1000)*x["duration"]
        totalCost += estimate_electricity_cost_for_run(
            x["start"], x["duration"], (x["consumption"]*x["duration"])/1000)
        print(x["start"], ":00 -", (x["start"]+x["duration"]),
              ":00 ", x["name"], " - ", (x["consumption"]/1000), "kWh")
    print("Total energy consumption:", round(totalConsumption, 4),
          "kWh\nTotal energy cost:", round(totalCost/1000, 2), "nok")
