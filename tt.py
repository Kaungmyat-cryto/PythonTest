

Major = input("IT , Civil , Mech , Mce , Electric \n Select the Major :  ")
Year = input("Enter the year :")


report=list()
galpha=list()
def item(name,roll,Myanmar, English, Math, Physic, Chem,Major):
    additem=[name,roll,Myanmar,English, Math, Physic, Chem,Major]
    report.append(additem)
    grade=[Myanmar,English, Math, Physic, Chem,Major]
    for i in grade:
        if i >= 90 and i <= 100:
            galpha.append('A')
        elif i >= 80 and i <= 89:
            galpha.append('B')
        elif i >= 70 and i <= 79:
            galpha.append('C')
        elif i >= 60 and i <= 69:
            galpha.append('D')
        elif i >= 50 and i <= 59:
            galpha.append('E')
        else:
            galpha.append('F')


# def showreport():
#     for reports in report:
#         print("Name \t%s\nRoll No\t%d"%(reports[0],reports[1],))
#         print("Myanmar\t % d(%s)\nEnglish\t % d(%s)\nMath\t % d(%s)"%(reports[2],galpha[0],reports[3],galpha[1],reports[4],galpha[2]))
#         print("Physics:\t %d(%s)\nChemistry:\t %d(%s)"%(reports[5],galpha[3],reports[6],galpha[4]))
#         print(Major,":\t%d(%s)\n"%(reports[7],galpha[5]))

class Student:

    def __init__(self,name='',roll='',Myanmar=0,English=0,Math=0,Physic=0,Chem=0):
        self.__name=name
        self.__roll=roll
        self.__Myanmar=Myanmar
        self.__English=English
        self.__Math3=Math
        self.__Physic=Physic
        self.__Chem=Chem

    def showreport(self):
        for reports in report:
            print("Name \t%s\nRoll No\t%d" % (reports[0], reports[1],))
            print("Myanmar\t % d(%s)\nEnglish\t % d(%s)\nMath\t % d(%s)" % (
            reports[2], galpha[0], reports[3], galpha[1], reports[4], galpha[2]))
            print("Physics:\t %d(%s)\nChemistry:\t %d(%s)" % (reports[5], galpha[3], reports[6], galpha[4]))
            print(Major, ":\t%d(%s)\n" % (reports[7], galpha[5]))

    def getmark(self):
        name=str(input("Enter the student name:"))
        self.name=name
        roll=int(input("Enter the roll number :"))
        self.roll=roll
        Myanmar=int(input("Enter the marks of Myanmar :"))
        self.Myanmar=Myanmar
        English = int(input("Enter the marks of English :"))
        self.English = English
        Math = int(input("Enter the marks of Math :"))
        self.Math = Math
        Physic = int(input("Enter the marks of Physic :"))
        self.Physic = Physic
        Chem = int(input("Enter the marks of Chem :"))
        self.Chem = Chem
        Major = int(input("Enter the marks of ,Major "))
        self.Major = Major



class First(Student):
    def __init__(self, name='', roll='', Myanmar=0, English=0, Math=0, Physic=0, Chem=0):
        super().__init__(name,roll,Myanmar, English, Math, Physic, Chem)
        self.__Major = Major

    def getmark(self):
        while True:
            super().getmark()
            item(self.name,self.roll,self.Myanmar,self.English,self.Math,self.Physic,self.Chem,self.Major)
            choice = input('Would you like to add more?(y/n): ')
            if choice == 'y':
                continue
            else:
                super().showreport()
                exit(0)

if (Major=='IT' or 'Civil' or 'Electric' or 'Mce' or 'Mech') and (Year=='1'):
    h1=First()
    h1.getmark()
else:
    print("Something worng!")
    exit()