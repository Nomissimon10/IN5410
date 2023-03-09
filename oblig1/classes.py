import random
from appliances import appliances


class Appliance:
    # usageTime = Hours daily usage, time = timeslot for usage to happen within
    def __init__(self, name, type, minkW, maxkW, duration, timeStart, timeStop):
        self.name = name
        if type is 0:
            self.type = "non-shiftable"
        elif type is 1:
            self.type = "shiftable"
        elif type is 2:
            self.type = "random"
        else:
            raise Exception("Type must be 0, 1 or 2")
        self.duration = duration
        self.timeStart = timeStart
        self.timeStop = timeStop
        if maxkW is None:
            self.consumption = minkW
        else:
            self.consumption = self.randomize_usage_between(minkW, maxkW)

    def randomize_usage_between(self, min, max):
        return random.randint(min, max)

    def __str__(self):
        return f"{self.name} ({self.consumption}W) \nDaily use: {self.duration} hours in timeslot {self.timeStart}-{self.timeStop}\n"

    def getType(self):
        return self.type


# * DESCRIPTION: Creates appliance objects
# * INPUT:
# * OUTPUT: List of appliance objects.
def createAppliances() -> list:
    allAppliances = []
    for a in appliances:
        allAppliances.append(Appliance(a, (appliances[a][0]), (appliances[a][1]), (
            appliances[a][2]), (appliances[a][3]), (appliances[a][4]), (appliances[a][5])))
    return allAppliances
