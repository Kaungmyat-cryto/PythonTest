Major = input("IT , Civil , Mech , Electronic , Electric\n Select the Major :  ")
Year = input("Enter the year :")
subject=list()
report=list()
galpha=list()
class Student:

    def item(self,name='',roll=0,sub1=0,sub2=0,sub3=0,sub4=0,sub5=0,sub6=0,sub7=0):
        additem=[name,roll,sub1,sub2,sub3,sub4,sub5,sub6,sub7]
        report.append(additem)
        grade=[sub1,sub2,sub3,sub4,sub5,sub6,sub7]
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


    def __init__(self,name='',roll='',sub1=0,sub2=0,sub3=0,sub4=0,sub5=0,sub6=0,sub7=0):
        if (Year == '1')and (Major=='IT'or Major=='Civil'or Major=='Mech'or Major=="Electric"or Major=='Electronic'):
            sub = ('Myanmar','English','Mathematic','Physic','Chemical','Drawing',Major)
        # elif Year =='2' and Major=='IT':
        #     sub1='English'
        #     sub2 = 'Engineering MathematicsIII'
        #     sub3 = 'Basic Electricity and Electronics'
        #     sub4 = 'Digital Logic Design'
        #     sub5 = 'Programming Language in C++'
        #     sub6 = 'Data Communications'
        #     sub7 = 'Web develpment Technology'
        #     subject =[sub1, sub2, sub3, sub4, sub5, sub6, sub7]
        # elif Year=='2' and Major=="Civil":
        #     sub1='English'
        #     sub2='Engineering Mathematics III,IV'
        #     sub3='surveying I,II'
        #     sub4='Applied Electrical engineering I,II'
        #     sub5='Engineering Mechanics'
        #     sub6='Workshop technologies and practies I,II'
        #     sub7='Civil Engineering drawing I,II'
        #     subject = (sub1, sub2, sub3, sub4, sub5, sub6, sub7)
        # else :
            print ("something wrong ....")
            exit()
        self.__name = name
        self.__roll = roll
        self.__sub1 = sub1
        self.__sub2 = sub2
        self.__sub3 = sub3
        self.__sub4 = sub4
        self.__sub5 = sub5
        self.__sub6 = sub6
        self.__sub7 = sub7
    def printing(self):
        for reports in report:
            print("Name :%s\nRoll No :\t%d\n" % (reports[0], reports[1]))
            print("%s:\t %d(%s)\n" % (subject[0],reports[2], galpha[0]))
            print("%s:\t %d(%s)\n" % (subject[1],reports[3], galpha[1]))
            print("%s:\t %d(%s)\n" % (subject[2],reports[4], galpha[2]))
            print("%s:\t %d(%s)\n" % (subject[3],reports[5], galpha[3]))
            print("%s:\t %d(%s)r\n" % (subject[4],reports[6], galpha[4]))
            print("%s:\t %d(%s)\n" % (subject[5],reports[7], galpha[5]))
            print("%s:\t %d(%s)\n" % (subject[6],reports[8], galpha[6]))


    def getmark(self):
        name=str(input("Enter the student name:"))
        self.name=name
        roll=int(input("Enter the roll number :"))
        self.roll=roll
        sub1=int(input("Enter the marks of{}:".format(sub[0])))
        self.__sub1=sub1
        sub2 = int(input("Enter the marks of {}:".format(self.__sub2)))
        self.__sub2=sub2
        sub3 = int(input("Enter the marks of {}:".format(self.__sub3)))
        self.__sub3=sub3
        sub4 = int(input("Enter the marks of {}:".format(self.__sub4)))
        self.__sub4=sub4
        sub5 = int(input("Enter the marks of {}:".format(self.__sub5)))
        self.__sub5=sub5
        sub6 = int(input("Enter the marks of {}:".format(self.__sub6)))
        self.__sub6 = sub6
        sub7 = int(input("Enter the marks of {}:".format(self.__sub7)))
        self.__sub7= sub7


class Real(Student):
    def __init__(self, name='', roll='', sub1=0, sub2=0, sub3=0, sub4=0, sub5=0, sub6=0, sub7=0):
        super().__init__(name,roll,sub1,sub2,sub3,sub4,sub5,sub6,sub7)

    def getmark(self):
        while True:
            super().getmark()
            super().item()
            choice = input('Would you like to add more?(y/n): ')
            if choice == 'y':
                continue
            else:
                super().printing()
                exit(0)

h1=Real()
h1.getmark()


