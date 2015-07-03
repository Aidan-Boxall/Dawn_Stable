class Time:
    def __init__(self, hrs=0, mins=0):
        self.hrs = hrs + mins/60
        self.hrs = hrs%24
        self.mins = mins%60


    def add_one_min(self):
        self.mins += 1
        if self.mins >=60:
            self.hrs += mins/60
            self.mins = mins%60
        self.hrs = self.hrs%24


    def __str__(self):
        return '{0:02.0F}:{1:02.0F}'.format(self.hrs,self.mins)


    def __add__(self, t):
        if isinstance(t, int):
            t = Time(0,t)
        hrs = self.hrs + t.hrs
        mins = self.mins + t.mins
        return Time(hrs, mins)


    def __iadd__(self,t):
        if isinstance(t, int):
            t = Time(0,t)
        hrs = self.hrs + t.hrs
        mins = self.mins + t.mins
        return Time(hrs, mins)


    def __radd__(self, t):
        if isinstance(t, int):
            t = Time(0,t)
        hrs = self.hrs + t.hrs
        mins = self.mins + t.mins
        if mins >= 60:
            hrs += mins/60
            mins = mins%60
        return Time(hrs, mins)


t1 = Time(23,30)
t1.add_one_min()
t2 = Time(2,45)
t3 = 35 + t1
print t3