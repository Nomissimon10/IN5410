import random


class Appliance:
    # usageTime = Hours daily usage, time = timeslot for usage to happen within
    def __init__(self, name, shiftable, minkW, maxkW, duration, timeStart, timeStop):
        self.name = name
        self.shiftable = shiftable
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
        return f"{self.name} ({self.consumption} kW) \nDaily use: {self.duration} hours in timeslot {self.timeStart}-{self.timeStop}\n"


class Household:

    def __init__(self, id):
        self.id = id
        self.allAppliances = []
        self.nonShiftable = None
        self.shiftable = None
        self.auxilary = None

    def setNonShiftable(self, list):
        self.nonShiftable = list
        for a in list:
            if a not in self.allAppliances:
                self.allAppliances.append(a)

    def setShiftable(self, list):
        self.shiftable = list
        for a in list:
            if a not in self.allAppliances:
                self.allAppliances.append(a)

    def setAuxilary(self, list):
        self.auxilary = list
        for a in list:
            if a not in self.allAppliances:
                self.allAppliances.append(a)

    def randomizeAppliances(appliances: list) -> list:
        return random.sample(appliances, random.randint(1, len(appliances)))

    def removeEV(self):
        for a in self.allAppliances:
            if a.name == "ev":
                self.allAppliances.remove(a)
                self.shiftable.remove(a)

    def printAllHouseholdAppliances(self):
        print("Household has", len(
            self.allAppliances), "appliances.")
        for a in self.allAppliances:
            print("----")
            print(a)
