class Time:
    def __init__(self,hour=0,min=0,sec=0):
        self.__hour=hour
        self.__min=min
        self.__sec=sec

    def get_time(self):
        hour=int(input("Enter the hour :"))
        self.hour=hour
        min=int(input("Enter the minutes :"))
        self.min=min
        sec=int(input("Enter the second :"))
        self.sec=sec

    def change_hr(self,time):
        hr = time // 3600
        min = (time % 3600) // 60
        sec = (time % 3600) % 60
        print("Time :%d:%d:%d" % (hr, min, sec))

    def __sub__(self,other):
        time1=self.hour*3600+self.min*60+self.sec
        time2=other.hour*3600+other.min*60+other.sec
        if time1>time2:
            time=time1-time2
            Time.change_hr(self,time)
        else:
            time=time2-time1
            Time.change_hr(self,time)

    def __add__(self,other):
        time1 = self.hour * 3600 + self.min * 60 + self.sec
        time2 = other.hour * 3600 + other.min * 60 + other.sec
        time=time1+time2
        Time.change_hr(self,time)

T1=Time()
T1.get_time()
T2=Time()
T2.get_time()
print("after subtracting:")
(T1-T2)
print("after adding:")
(T1+T2)
