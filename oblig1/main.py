from plotPriceScheme import plotTable
from generateElectricityPrices import generate_electricity_prices

from appliances import nonShiftable, shiftable, auxilary
from classes import Appliance, Household

from optimal import optimal_calculation, calculate_schedule_cost, print_schedule

import random


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
    household = Household()
    household.setNonShiftable(nonShiftableAppliances)
    household.setShiftable(shiftableAppliances)
    household.setAuxilary(randomizeList(auxilaryAppliances))
    household.printAllHouseholdAppliances()
    # Create and print schedule
    householdSchedule = optimal_calculation(household.allAppliances)
    print_schedule(householdSchedule)
    print(f'{calculate_schedule_cost(householdSchedule)}nok for this schedule')

    # * Assignment 3
    print("Assignment 3 \n-----------------------------------------------------------------")
    neigborhoodAppliances = []
    n = 4
    # Create N number of households
    for i in range(n):
        household = Household()
        household.setNonShiftable(nonShiftableAppliances)
        household.setShiftable(shiftableAppliances)
        household.setAuxilary(randomizeList(auxilaryAppliances))
        # Household has a 75% chance of NOT having a EV
        x = random.randint(0, 4)
        if x == 0:
            household.removeEV()
        # Adds households appliances to neighborhood total appliances
        for a in household.allAppliances:
            neigborhoodAppliances.append(a)

    neighborhoodSchedule = optimal_calculation(neigborhoodAppliances)
    print_schedule(neighborhoodSchedule)
    print(f'{calculate_schedule_cost(neighborhoodSchedule)}nok for this schedule')


def randomizeList(list):
    return random.sample(list, random.randint(1, len(list)))


main()
