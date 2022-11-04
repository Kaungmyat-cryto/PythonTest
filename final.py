Major = input("IT , Civil , Mech , Electronic , Electric\n Select the Major :  ")
Year = input("Enter the year :")


galpha=list()

subject=list()
if (Year == '1') and (
        Major == 'IT' or Major == 'Civil' or Major == 'Mech' or Major == "Electric" or Major == 'Electronic'):
    sub1 = 'Myanmar'
    sub2 = 'English'
    sub3 = 'Mathematic'
    sub4 = 'Physic'
    sub5 = 'Chemical'
    sub6 = 'Drawing'
    sub7 = Major
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '2' and Major == 'IT':
    sub1 = 'English'
    sub2 = 'Engineering MathematicsIII'
    sub3 = 'Basic Electricity and Electronics'
    sub4 = 'Digital Logic Design'
    sub5 = 'Programming Language in C++'
    sub6 = 'Data Communications'
    sub7 = 'Web develpment Technology'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '2' and Major == "Civil":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics III,IV'
    sub3 = 'surveying I,II'
    sub4 = 'Applied Electrical engineering I,II'
    sub5 = 'Engineering Mechanics'
    sub6 = 'Workshop technologies and practies I,II'
    sub7 = 'Civil Engineering drawing I,II'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '3' and Major == "Civil":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics V,VI'
    sub3 = 'surveying III'
    sub4 = 'Mechanics of Materials I,II'
    sub5 = 'Fluid mechanics I,II'
    sub6 = 'Transportation Engineering I,II'
    sub7 = 'Engineering Geology I,II'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '4' and Major == "Civil":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics VII,VIII'
    sub3 = 'Theory of Structures I, II'
    sub4 = 'Design of Timber Structures'
    sub5 = 'Foundation Engineering'
    sub6 = 'Hydraulic Engineering and Applied Hydraulic I, II'
    sub7 = 'Transportation Engineering III,IV'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '5' and Major == "Civil":
    sub1 = 'Construction Engineering Management I, II'
    sub2 = 'Theory of Structures III'
    sub3 = 'Design of Reinforced Concrete Structure I,II'
    sub4 = 'Design of Hydraulic Structure I,II'
    sub5 = 'Environmental Engineering I,II'
    sub6 = 'Estimating and Specification I,II'
    sub7 = 'Design of Street Structure I'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '2' and Major == "Mech":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics III,IV'
    sub3 = 'Engineering Materials'
    sub4 = 'Applied Electrical Engineering I,II'
    sub5 = 'Engineering Mechanics'
    sub6 = 'Workshop Technology'
    sub7 = 'Machine Drawing'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '3' and Major == "Mech":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics V,VI'
    sub3 = 'Theory of Machines I'
    sub4 = 'Strength of Materials'
    sub5 = 'Engineering Materials'
    sub6 = 'Analogue and Digital ElectronicsI,I'
    sub7 = 'Production Technology'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '4' and Major == "Mech":
    sub1 = 'English'
    sub2 = 'Engineering Mathematics VI,VII'
    sub3 = 'Design of Machine Elements'
    sub4 = 'Manufacturing System and Automations'
    sub5 = 'Heat Transfer'
    sub6 = 'Strength of Materials II'
    sub7 = 'Theory of Machines II'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]
elif Year == '5' and Major == "Mech":
    sub1 = 'Engineering Management'
    sub2 = 'Internal Combustion Engines'
    sub3 = 'Refrigeration and Air Conditioning'
    sub4 = 'Strength of Materials'
    sub5 = 'Vibration and Controls'
    sub6 = 'Fluid Mechanics II'
    sub7 = 'Gas Turbine Theory'
    subject = [sub1, sub2, sub3, sub4, sub5, sub6, sub7]



else:
    print("something wrong ....")
    exit()
report=list()
def item(name,roll,sub1,sub2,sub3,sub4,sub5,sub6,sub7,Total,avg):
    additem=[name,roll,sub1,sub2,sub3,sub4,sub5,sub6,sub7,Total,avg]
    report.append(additem)
    grade=[sub1,sub2,sub3,sub4,sub5,sub6,sub7,avg]
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
class Student:


    def __init__(self,name='',roll='',sub1=0,sub2=0,sub3=0,sub4=0,sub5=0,sub6=0,sub7=0,Total=0,avg=0):
        self.__name = name
        self.__roll = roll
        self.__sub1 = sub1
        self.__sub2 = sub2
        self.__sub3 = sub3
        self.__sub4 = sub4
        self.__sub5 = sub5
        self.__sub6 = sub6
        self.__sub7 = sub7
        self.__Total=Total
        self.__avg=avg
    def printing(self):
        for reports in report:
            print("Name :%s\nRoll No :\t%d\n" % (reports[0], reports[1]))
            print("%s:\t %d(%s)\n" % (subject[0],reports[2], galpha[0]))
            print("%s:\t %d(%s)\n" % (subject[1],reports[3], galpha[1]))
            print("%s:\t %d(%s)\n" % (subject[2],reports[4], galpha[2]))
            print("%s:\t %d(%s)\n" % (subject[3],reports[5], galpha[3]))
            print("%s:\t %d(%s)\n" % (subject[4],reports[6], galpha[4]))
            print("%s:\t %d(%s)\n" % (subject[5],reports[7], galpha[5]))
            print("%s:\t %d(%s)\n" % (subject[6],reports[8], galpha[6]))
            print("Total :%d\nAverage :%d(%s)" %(reports[9],reports[10],galpha[7]))


    def getmark(self):
        name=str(input("Enter the student name:"))
        self.name=name
        roll=int(input("Enter the roll number :"))
        self.roll=roll
        sub1=int(input("Enter the marks of {}:".format(subject[0])))
        self.sub1=sub1
        sub2 = int(input("Enter the marks of {}:".format(subject[1])))
        self.sub2=sub2
        sub3 = int(input("Enter the marks of {}:".format(subject[2])))
        self.sub3=sub3
        sub4 = int(input("Enter the marks of {}:".format(subject[3])))
        self.sub4=sub4
        sub5 = int(input("Enter the marks of {}:".format(subject[4])))
        self.sub5=sub5
        sub6 = int(input("Enter the marks of {}:".format(subject[5])))
        self.sub6 = sub6
        sub7 = int(input("Enter the marks of {}:".format(subject[6])))
        self.sub7= sub7
        Total=sub1+sub2+sub3+sub4+sub5+sub6+sub7
        self.Total=Total
        avg=Total/7
        self.avg=avg


class Real(Student):
    def __init__(self, name='', roll='', sub1=0, sub2=0, sub3=0, sub4=0, sub5=0, sub6=0, sub7=0,Total=0,avg=0):
        super().__init__(name,roll,sub1,sub2,sub3,sub4,sub5,sub6,sub7,Total,avg)

    def getmark(self):
        while True:
            super().getmark()
            item(self.name,self.roll,self.sub1,self.sub2,self.sub3,self.sub4,self.sub5,self.sub6,self.sub7,self.Total,self.avg)
            choice = input('Want to add more?(y/n): ')
            if choice == 'y':
                continue
            else:
                super().printing()
                exit(0)

h1=Real()
h1.getmark()


