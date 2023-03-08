from plotPriceScheme import plotTable
from generateElectricityPrices import generate_electricity_prices

from appliances import nonShiftable, shiftable, random
from classes import Appliance

#Using main to create and test objects
def main():
    allAppliances = []
    nonShiftableAppliances = []
    shiftableAppliances = []
    randomAppliances = []

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

    for key in random:
        newAppliance = Appliance(key, (random[key][0]), (random[key][1]), (random[key]
                                 [2]), (random[key][3]), (random[key][4]), (random[key][5]))
        allAppliances.append(newAppliance)
        randomAppliances.append(newAppliance)

    for a in allAppliances:
        print(a)


main()
