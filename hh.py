class Parent:

    def __init__(self,Myanmar=0,English=0,Math=0,Physic=0,Chem=0):
        self.__Myanmar = Myanmar
        self.__English = English
        self.__Math3 = Math
        self.__Physic = Physic
        self.__Chem = Chem

    # def Grading(self):
    #     if self >= 90 and self <= 100:
    #         return 'A'
    #     elif self >= 80 and self <= 89:
    #         return 'B'
    #     elif self >= 70 and self <= 79:
    #         return 'C'
    #     elif self >= 60 and self <= 69:
    #         return 'D'
    #     elif self >= 50 and self <= 59:
    #         return 'E'
    #     else:
    #         return 'F'

    def getmark(self):

        Myanmar = int(input("Enter the marks of Myanmar :"))
        self.Myanmar = Myanmar
        English = int(input("Enter the marks of English :"))
        self.English = English
        Math = int(input("Enter the marks of Math :"))
        self.Math = Math
        Physic = int(input("Enter the marks of Physic :"))
        self.Physic = Physic
        Chem = int(input("Enter the marks of Chem :"))
        self.Chem = Chem
        getmark = [Myanmar, English, Math, Physic, Chem]
        for i in getmark:
            if i >= 90 and i <= 100:
                print(i ,"a")
            elif i >= 80 and i <= 89:
                print (i ,'B')
            elif i >= 70 and i <= 79:
                print (i ,'C')
            elif i >= 60 and i <= 69:
                print(i ,'D')
            elif i >= 50 and i <= 59:
                print (i ,'E')
            else:
                print (i ,'F')




h1=Parent()
h1.getmark()