# class university:
#     def __init__(self,name='Error',nrc=0,feet=0,inches=0.0):
#         self.__name = name
#         self.__nrc = nrc
#         self.__feet = feet
#         self.__inches = inches
#
#     def get_name(self):
#         nm=str(input("Enter the name: "))
#         self.__name=nm
#
#     def get_nrc(self):
#         nrc=int(input("Enter the NRC: "))
#         self.__nrc=nrc
#
#     def get_height(self):
#         ft = int(input("Enter feet: "))
#         self.__feet =ft
#         inch = float(input("Enter inches: "))
#         self.__inches = inch
#
#     def print_uni(self):
#         print("Name :{0} \nNRC :{1} \nHeight :{2}-{3}" .format(self.__name,self.__nrc,self.__feet,self.__inches))
#
#
# uni = university()
# uni.get_name()
# uni.get_height()
# uni.get_nrc()
#
# uni.print_uni()
#
#
# class student(university):
#     def __init__(self,roll=0,year=0,name='Error',nrc=0,feet=0,inches=0.0):
#         self.__roll=roll
#         self.__year=year
#         super().__init__(name, nrc, feet, inches)
#
#
#
#     def get_roll(self):
#         roll=int(input("Enter the roll number :"))
#         self.__roll=roll
#
#     def get_year(self):
#         year=int(input("Enter the year :"))
#         self.__year=year
#
#     def print_stu(self):
#         print("roll :{0}\nyear :{1}".format(self.__roll, self.__year))
#         super().print_uni()
#
#
# stu=student()
# stu.get_name()
# stu.get_height()
# stu.get_nrc()
# stu.get_roll()
# stu.get_year()
# stu.print_stu()
#
#
# class teacher(university):
#
#     def __init__(self,subject="none",name='Error',nrc=0,feet=0,inches=0.0):
#         super().__init__(name,nrc,feet,inches)
#         self.__subject=subject
#
#     def get_sub(self):
#         sub=str(input("Enter the subject: "))
#         self.__subject=sub
#
#     def print_tr(self):
#         print("subject :%s" %(self.__subject))
#         super().print_uni()
# tr=teacher()
# tr.get_name()
# tr.get_sub()
# tr.get_nrc()
# tr.get_height()
# tr.print_tr()


class Grade:
    # constructor will pass the parameters to the CalGrade function
    def __init__(self, first, second, third,
                 fourth, fifth):

        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth

    def CalGrade(self):

        # Average is calculated
        average = (self.first + self.second + self.third
                   + self.fourth + self.fifth) / 5

        print(" Your average is ", average)

        # average is checked for evaluating the Grade of the student
        if (90 <= average <= 100):

            print(" You have obtained Grade A ")

        elif (80 <= average < 90):

            print(" You have obtained Grade B ")

        elif (70 <= average < 80):

            print(" You have obtained Grade C ")

        elif (60 <= average < 70):

            print(" You have obtained Grade D ")

        else:

            print(" You have obtained Grade F ")


if __name__ == "__main__":
    first = int(input(" Enter the marks obtained in first subject: "))
    second = int(input(" Enter the marks obtained in second subject: "))
    third = int(input(" Enter the marks obtained in third subject: "))
    fourth = int(input(" Enter the marks obtained in fourth subject: "))
    fifth = int(input(" Enter the marks obtained in fifth subject: "))
    # Object is created for class Grade
    Grade_obj = Grade(first, second, third, fourth, fifth)
    # CalGrade function is called
    Grade_obj.CalGrade()
