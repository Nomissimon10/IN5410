# Object structure: name:shiftable(bool), minW, maxW, hrs daily usage, not used before, not used after

nonShiftable = {
    "lighting": [False, 1000, 2000, 10, 10, 20],
    "heathing": [False, 6400, 9600, 24, 0, 24],
    "refrigerator": [False, 1320, 3960, 24, 0, 24],
    "freezer": [False, 1320, None, 24, 0, 24],
    "stove": [False, 3900, None, 2, 16, 20],
    "tv": [False, 150, 600, 5, 16, 23],
    "computer": [False, 600, None, 4, 16, 23]
}

shiftable = {
    "dishwasher": [True, 1440, None, 3, 0, 23],
    "laundry": [True, 1940, None, 2, 0, 23],
    "dryer": [True, 2500, None, 2, 0, 23],
    "ev": [True, 9900, None, 4, 0, 23]
}

auxilary = {
    "coffemaker": [True, 2.4, None, 1, 6, 8],
    "celingfan": [True, 55, 100, 4, 10, 18],
    "hairdryer": [True, 800, 1800, 1, 6, 8],
    "toaster": [True, 800, 1500, 1, 6, 8],
    "microwave": [True, 850, 1800, 1, 0, 24],
    "router": [True, 2, 20, 24, 0, 24],
    "cellphonecharger": [True, 2, 6, 4, 0, 24],
    "clothiron": [True, 800, 2000, 1, 20, 24]
}
