class height:
    def __init__(self,feet=0,inches=0.0):
        self.__feet=feet
        self.__inches=inches
    def get_height(self):
        ft = int(input("Enter feet: "))
        self.feet =ft
        inch = float(input("Enter inches: "))
        self.inches = inch

    def __str__(self):
        return "%d-%f"%(self.feet,self.inches)

    def __sub__(self,other):
        self.feet=self.feet+self.inches/12
        other.feet=other.feet+other.inches/12
        total=self.feet+other.feet

        return total


h1=height()
h1.get_height()
h2=height()
h2.get_height()
print("Height 1:",h1)
print("Height 2:",h2)
print(h2-h1)
