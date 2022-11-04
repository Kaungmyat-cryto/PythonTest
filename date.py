class Date:
    def __init__(self,day=0,month=0,year=0):
        self.__day=day
        self.__month=month
        self.__year=year

    def get_date(self):
        day=int(input("Enter the date :"))
        self.day=day
        month = int(input("Enter the month :"))
        self.month=month
        year=int(input("Enter the year :"))
        self.year=year

    def __str__(self):
        return "%d/%d/%d"%(self.day,self.month,self.year)

    def __lt__(self,other):
        if self.year<other.__year:
            return "Date 1 is less than Date 2"
        elif self.month<other.__month:
            return "Date 1 is less than Date 2"
        elif self.day<other.__day:
            return "Date 1 is less than Date 2"
        else:
            return "Date 1 isn't less than Date 2"


d1=Date()
d1.get_date()
d2=Date()
d2.get_date()
print('Date 1 :',d1)
print("Date 2 :",d2)
print(d1>d2)