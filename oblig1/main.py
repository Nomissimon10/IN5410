from appliances import nonShiftable, shiftable, auxilary
from classes import Appliance, Household
from optimal import optimal_calculation, calculate_schedule_cost, print_schedule, scheduleAppliances, optimizeSchedule, print_scedule_2

import random
from plotPriceScheme import plotHourlyConsumptionForHousehold, plotHouseholdUsages


# * Create all appliances
allAppliances = []
nonShiftableAppliances = []
shiftableAppliances = []
auxilaryAppliances = []

for key in nonShiftable:
    newAppliance = Appliance(key, (nonShiftable[key][0]), (nonShiftable[key][1]), (nonShiftable[key]
                                                                                   [2]), (nonShiftable[key][3]), (nonShiftable[key][4]), (nonShiftable[key][5]))
    allAppliances.append(newAppliance)
    nonShiftableAppliances.append(newAppliance)

for key in shiftable:
    newAppliance = Appliance(key, (shiftable[key][0]), (shiftable[key][1]), (shiftable[key]
                                                                             [2]), (shiftable[key][3]), (shiftable[key][4]), (shiftable[key][5]))
    allAppliances.append(newAppliance)
    shiftableAppliances.append(newAppliance)

for key in auxilary:
    newAppliance = Appliance(key, (auxilary[key][0]), (auxilary[key][1]), (auxilary[key]
                                                                           [2]), (auxilary[key][3]), (auxilary[key][4]), (auxilary[key][5]))
    allAppliances.append(newAppliance)
    auxilaryAppliances.append(newAppliance)


def task2():
    global allAppliances
    global nonShiftableAppliances
    global shiftableAppliances
    global auxilaryAppliances

    print("Assignment 2 \n-----------------------------------------------------------------")
    # Create household with all nonshiftable, all shiftable, and random auxilary appliances
    household = Household(1)
    household.setNonShiftable(nonShiftableAppliances)
    household.setShiftable(shiftableAppliances)
    household.setAuxilary(randomizeList(auxilaryAppliances))
    # household.printAllHouseholdAppliances()
    # Create and print schedule
    householdSchedule = optimal_calculation(household.allAppliances)
    print_schedule(householdSchedule)
    print(f'{calculate_schedule_cost(householdSchedule)}nok for this schedule')
    plotHourlyConsumptionForHousehold(
        householdSchedule, household.allAppliances)


def task3():
    global allAppliances
    global nonShiftableAppliances
    global shiftableAppliances
    global auxilaryAppliances

    print("Assignment 3 \n-----------------------------------------------------------------")
    neigborhoodAppliances = []
    n = 30
    # Create N number of households
    usage = []
    for i in range(n):
        household = Household(i + 1)
        household.setNonShiftable(nonShiftableAppliances)
        household.setShiftable(shiftableAppliances)
        household.setAuxilary(randomizeList(auxilaryAppliances))
        # Household has a 20% chance of having a EV
        x = random.randint(0, 5)
        if x != 0:
            household.removeEV()
        # Adds households appliances to neighborhood total appliances
        for a in household.allAppliances:
            neigborhoodAppliances.append(a)
        # Create and print household schedule
        householdSchedule = optimal_calculation(household.allAppliances)
        print("Household", household.id)
        print_schedule(householdSchedule)
        print(
            f'Household energy cost: {calculate_schedule_cost(householdSchedule)}nok\n--------------------------------------------')
        usage.append(householdSchedule)

    neighborhoodSchedule = optimal_calculation(neigborhoodAppliances)
    plotHouseholdUsages(usage)
    print(
        f'Total neighborhood cost: {calculate_schedule_cost(neighborhoodSchedule)}nok\n')


def task4():
    global allAppliances
    global nonShiftableAppliances
    global shiftableAppliances
    global auxilaryAppliances

    print("Assignment 4 \n-----------------------------------------------------------------")
    household = Household(1)
    household.setNonShiftable(nonShiftableAppliances)
    household.setShiftable(shiftableAppliances)
    household.setAuxilary(randomizeList(auxilaryAppliances))

    schedule = scheduleAppliances(household.allAppliances)
    optimized_schedule = optimizeSchedule(schedule)

    opt_schedule = {}
    for key in range(24):
        opt_schedule[key] = []

    index = 0
    for i in optimized_schedule:
        opt_schedule[i["start"]].append(household.allAppliances[index])
        index += 1

    print_scedule_2(optimized_schedule)
    plotHourlyConsumptionForHousehold(opt_schedule, household.allAppliances)


def main():
    # * Assignment 2
    task2()

    # * Assignment 3
    task3()

    # * Assignment 4
    task4()


def randomizeList(list):
    return random.sample(list, random.randint(1, len(list)))


main()
