class university:
    def __init__(self,name='Error',nrc=0,feet=0,inches=0.0):
        self.__name = name
        self.__nrc = nrc
        self.__feet = feet
        self.__inches = inches

    def get_name(self):
        nm=str(input("enter the name: "))
        self.__name=nm

    def get_nrc(self):
        nrc=int(input("enter the NRC: "))
        self.__nrc=nrc

    def get_height(self):
        ft = int(input("enter feet: "))
        self.__feet =ft
        inch = int(input("enter inches: "))
        self.__inches = inch

    def print_uni(self):
        print("Name :{0} \nNRC :{1} \nHeight :{2}-{3}" .format(self.__name,self.__nrc,self.__feet,self.__inches))

uni=university()
uni.get_name()
uni.get_height()
uni.get_nrc()

uni.print_uni()


class student(university):
    def __init__(self,roll=0,year=0,name='Error',nrc=0,feet=0,inches=0.0):
        self.__roll=roll
        self.__year=year
        super().__init__(name, nrc, feet, inches)



    def get_roll(self):
        roll=int(input("Enter the roll number :"))
        self.__roll=roll

    def get_year(self):
        year=int(input("Enter the year :"))
        self.__year=year

    def print_stu(self):
        print("{0}\n""roll :{1}\nyear :{2}".format(super().print_uni(),self.__roll,self.__year))

stu=student()
stu.get_name()
stu.get_height()
stu.get_nrc()
stu.get_roll()
stu.get_year()
stu.print_stu()


class teacher(university):

    def __init__(self,subject="none",name='Error',nrc=0,feet=0,inches=0.0):
        super().__init__(name,nrc,feet,inches)
        self.__subject=subject

    def get_sub(self):
        sub=str(input("Enter the subject: "))
        self.__subject=sub

    def print_tr(self):
        print("%s\n %s" %(super().print_uni(),self.__subject))

tr=teacher()
tr.get_name()
tr.get_sub()
tr.get_nrc()
tr.get_height()
tr.print_tr()