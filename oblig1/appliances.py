# Object structure: name:shiftable(bool), minW, maxW, hrs daily usage, not used before, not used after

nonShiftable = {
    "Lighting": [False, 1000, 2000, 10, 10, 20],
    "Heating": [False, 6400, 9600, 24, 0, 24],
    "Refrigerator": [False, 1320, 3960, 24, 0, 24],
    "Freezer": [False, 1320, None, 24, 0, 24],
    "Stove": [False, 3900, None, 2, 16, 20],
    "TV": [False, 150, 600, 5, 16, 23],
    "Computer": [False, 600, None, 4, 16, 23]
}

shiftable = {
    "Dishwasher": [True, 1440, None, 3, 0, 23],
    "Laundromat": [True, 1940, None, 2, 0, 23],
    "Dryer": [True, 2500, None, 2, 0, 23],
    "EV": [True, 9900, None, 4, 0, 23]
}

auxilary = {
    "Coffeemaker": [True, 2.4, None, 1, 6, 8],
    "Ceiling-Fan": [True, 55, 100, 4, 10, 18],
    "Hairdryer": [True, 800, 1800, 1, 6, 8],
    "Toaster": [True, 800, 1500, 1, 6, 8],
    "Microwave": [True, 850, 1800, 1, 0, 24],
    "Router": [True, 2, 20, 24, 0, 24],
    "Cellphone-charger": [True, 2, 6, 4, 0, 24],
    "Cloth-iron": [True, 800, 2000, 1, 20, 24]
}
