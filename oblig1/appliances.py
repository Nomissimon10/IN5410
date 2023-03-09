
# * STRUCTURE: "name":["type, minkW, maxkW, time, timeslotStart, timeslotEnd"]
#   * type 0 = non-shiftable,
#   * type 1 = shiftable
#   * type 3 = random

appliances = {
    "lighting": [0, 1000, 2000, 10, 10, 20],
    "heathing": [0, 6400, 9600, 24, 0, 23],
    "refrigerator": [0, 1320, 3960, 24, 0, 23],
    "freezer": [0, 1320, None, 24, 0, 23],
    "stove": [0, 3900, None, 2, 16, 20],
    "tv": [0, 150, 600, 5, 16, 23],
    "computer": [0, 600, None, 4, 16, 23],
    "dishwasher": [1, 1440, None, 2, 0, 23],
    "laundry": [1, 1940, None, 1.5, 0, 23],
    "dryer": [1, 2500, None, 1.5, 0, 23],
    "ev": [1, 9900, None, 4, 0, 23],
    "coffemaker": [2, 2.4, None, 0.25, 6, 8],
    "celingfan": [2, 55, 100, 4, 10, 18],
    "hairdryer": [2, 800, 1800, 0.25, 6, 8],
    "toaster": [2, 800, 1500, 0.08, 6, 8],
    "microwave": [2, 850, 1800, 0.17, 0, 23],
    "router": [2, 2, 20, 24, 0, 23],
    "cellphone-charger": [2, 2, 6, 4, 0, 23],
    "clothing-iron": [2, 800, 2000, 0.5, 20, 23]
}
