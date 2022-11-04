from deeperlook.tt import student
class Secondyear(student):

    class IT(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, IT=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__IT = IT
        def getmark(self):
            while True:
                super().getmark()
                IT = int(input("Enter the marks of IT :"))
                self.IT = IT
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)


    class Mech(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, Mech=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__Mech = Mech

        def getmark(self):
            while True:
                super().getmark()
                Mech = int(input("Enter the marks of Mech :"))
                self.Mech = Mech
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)

    class Civil(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, civil=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__civil= civil

        def getmark(self):
            while True:
                super().getmark()
                civil = int(input("Enter the marks of Civil :"))
                self.civil = civil
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)

    class Electric(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, electric=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__electric=electric

        def getmark(self):
            while True:
                super().getmark()
                electric = int(input("Enter the marks of Electric :"))
                self.electric = electric
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)

    class Textile(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, Textile=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__Textile=Textile

        def getmark(self):
            while True:
                super().getmark()
                Textile = int(input("Enter the marks of Textile :"))
                self.Textile = Textile
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)

    class Chemical(student):
        def __init__(self, Myanmar=0, English=0, Math=0, Physic=0, Chem=0, Chemical=0):
            super().__init__(Myanmar, English, Math, Physic, Chem)
            self.__Chemical=Chemical

        def getmark(self):
            while True:
                super().getmark()
                chemical = int(input("Enter the marks of Chemical :"))
                self.Chemical = chemical
                choice = input('Would you like to add more?(y/n): ')
                if choice == 'y':
                    continue
                else:
                    exit(0)
if Year=='2'

