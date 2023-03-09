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
