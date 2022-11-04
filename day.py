class Date:
    def __init__(self,day=0,month=0,year=0):
        self.__day=day
        self.__month=month
        self.__year=year

    def __str__(self):
        return "%d:%d:%d"%(self.__day,self.__month,self.__year)

    def __lt__(self,other):
        if self.__year<other.__year:
            return True
        elif self.__month<other.__month:
            return True
        elif self.__day<other.__day:
            return True
        else:
            return False

Date()