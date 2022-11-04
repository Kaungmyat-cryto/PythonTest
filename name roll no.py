class name:
    def __init__(self,name='Error',roll=0):
        self.__name=name
        self.__roll=roll

    def get_info(self):
        nm=str(input("enter the name: "))
        self.__name=nm

    def get_roll(self):
        roll=int(input("enter the roll number: "))
        self.__roll=roll

    def print_name(self):
        print("Name: %s "%(self.__name))

    def print_roll(self):
        print("Roll number : %d" %(self.__roll))

Name=name()
Name.get_name()
Name.print_name()

Roll=name()
Roll.get_roll()
Roll.print_roll()