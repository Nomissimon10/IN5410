from appliances import nonShiftable, shiftable, auxilary
from classes import Appliance, Household
from optimal import optimal_calculation, calculate_schedule_cost, print_schedule, scheduleAppliances, optimizeSchedule

import random
from plotPriceScheme import plotHourlyConsumption


def main():
    # Create all appliances
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

    # * Assignment 2
    print("Assignment 2 \n-----------------------------------------------------------------")
    # Create household with all nonshiftable, all shiftable, and random auxilary appliances
    household = Household(1)
    household.setNonShiftable(nonShiftableAppliances)
    household.setShiftable(shiftableAppliances)
    household.setAuxilary(randomizeList(auxilaryAppliances))
    household.printAllHouseholdAppliances()
    # Create and print schedule
    householdSchedule = optimal_calculation(household.allAppliances)
    print_schedule(householdSchedule)
    print(f'{calculate_schedule_cost(householdSchedule)}nok for this schedule')
    plotHourlyConsumption(householdSchedule, household.allAppliances)

    # * Assignment 3
    print("Assignment 3 \n-----------------------------------------------------------------")
    neigborhoodAppliances = []
    n = 30
    # Create N number of households
    for i in range(n):
        household = Household(i + 1)
        household.setNonShiftable(nonShiftableAppliances)
        household.setShiftable(shiftableAppliances)
        household.setAuxilary(randomizeList(auxilaryAppliances))
        # Household has a 75% chance of having a EV
        x = random.randint(0, 4)
        if x == 0:
            household.removeEV()
        # Adds households appliances to neighborhood total appliances
        for a in household.allAppliances:
            neigborhoodAppliances.append(a)
        # Create and print household schedule
        householdScehdule = optimal_calculation(household.allAppliances)
        print("Household", household.id)
        print_schedule(householdScehdule)
        print(
            f'Household energy cost: {calculate_schedule_cost(householdScehdule)}nok\n--------------------------------------------')

    neighborhoodSchedule = optimal_calculation(neigborhoodAppliances)
    print(
        f'Total neighborhood cost: {calculate_schedule_cost(neighborhoodSchedule)}nok\n')

    # * Assignment 4
    print("Assignment 4 \n-----------------------------------------------------------------")
    household = Household(1)
    household.setNonShiftable(nonShiftableAppliances)
    household.setShiftable(shiftableAppliances)
    household.setAuxilary(randomizeList(auxilaryAppliances))

    sched = scheduleAppliances(household.allAppliances)
    optimizeSchedule(sched)


def randomizeList(list):
    return random.sample(list, random.randint(1, len(list)))


main()
