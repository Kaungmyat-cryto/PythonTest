class university:
    def __init__(self,name='Error',nrc=0,feet=0,inches=0.0):
        self.__name=name
        self.__nrc=nrc
        self.__feet = feet
        self.__inches = inches

    def get_info(self):
        nm=str(input("enter the name: "))
        self.__name=nm
        nrc=int(input("enter the NRC: "))
        self.__nrc=nrc
        ft = int(input("enter feet: "))
        self.__feet =ft
        inch = float(input("enter inches: "))
        self.__inches =inch

    def print_uni(self):
        print("Name:%s \nNRC:%d \nHeight:%d-%f"%(self.__name,self.__nrc,self.__feet,self.__inches))

uni=university()
uni.get_info()

uni.print_uni()


class student(university):
    def __init__(self,roll=0,year=0,name='Error',nrc=0,feet=0,inches=0.0):
        self.__roll=roll
        self.__year=year
        super().__init__(name, nrc, feet, inches)



    def get_stu(self):
        roll=int(input("Enter the roll number :"))
        self.__roll=roll
        year=int(input("Enter the year :"))
        self.__year=year


    def print_stu(self):
        super().print_uni()
        print("roll%d\nyear%d"%(self.__roll,self.__year))

stu=student()
stu.get_info()
stu.get_stu()


stu.print_stu()


class teacher(university):

    def __init__(self,subject="none",name='Error',nrc=0,feet=0,inches=0.0):
        super().__init__(name,nrc,feet,inches)
        self.__subject=subject

    def get_sub(self):
        sub=str(input("Enter the subject: "))
        self.__subject=sub

    def print_tr(self):
        print("%s\n%s"%(super().print_uni(),self.__subject))

tr=teacher()
tr.get_info()
tr.get_sub()
tr.print_tr()