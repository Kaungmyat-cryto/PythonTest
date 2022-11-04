# student=list()
# def marks(name='',age='',height='',address=''):
#     temp = [name,age,height,address]
#     student.append(temp)
#
#
# def show_profile():
#     for mark in student:
#         print("Name: \t%s\nAge: \t%d\nHeight: %.2f\nAddress: %s\n\n" % (mark[0],mark[1],mark[2],mark[3]))
#
#
# sub1=str(input("Enter name for 1st subject: "))
# sub2=input("Enter name for 2nd subject: ")
# sub3=input("Enter name for 3rd subject: ")
# sub4=input("Enter name for 4th subject: ")
# sub5=input("Enter name for 5th subject: ")
# sub6=input("Enter name for 6th subject: ")
#
# class Grading:
#     def __init__(self,mark1=0,mark2=0,mark3=0,mark4=0,mark5=0,mark6=0):
#         self.__mark1=mark1
#         self.__mark2=mark2
#         self.__mark3=mark3
#         self.__mark4=mark4
#         self.__mark5=mark5
#         self.__mark6=mark6
#
# # while True :
#     def getmark(self):
#         name=int(input("Enter the name :"))
#         self.name=name
#         mark1=int(input("Enter the marks of {} :".format(sub1)))
#         self.mark1=mark1
#         mark2 = int(input("Enter the marks of {} :".format(sub2)))
#         self.mark2 = mark2
#         mark3 = int(input("Enter the marks of {} :".format(sub3)))
#         self.mark3 = mark3
#         mark4 = int(input("Enter the marks of {} :".format(sub4)))
#         self.mark4 = mark4
#         mark5 = int(input("Enter the marks of {} :".format(sub5)))
#         self.mark5 = mark5
#         mark6 = int(input("Enter the marks of {} :".format(sub6)))
#         self.mark6 = mark6
#
#
# h1=Grading()
# h1.getmark()


#
#
jack = {"name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
        }

# 2. James's dictionary
james = {"name": "James Potter",
         "assignment": [82, 56, 44, 30],
         "test": [80, 80],
         "lab": [67.90, 78.72]
         }

# 3. Dylan's dictionary
dylan = {"name": "Dylan Rhodes",
         "assignment": [77, 82, 23, 39],
         "test": [78, 77],
         "lab": [80, 80]
         }

# 4. Jessica's dictionary
jess = {"name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
        }

# 5. Tom's dictionary
tom = {"name": "Tom Hanks",
       "assignment": [29, 89, 60, 56],
       "test": [65, 56],
       "lab": [50, 40.6]
       }


# Function calculates average
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


# Function calculates total average
def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
    lab = get_average(students["lab"])

    # Return the result based
    # on weightage supplied
    # 10 % from assignments
    # 70 % from test
    # 20 % from lab-works
    return (0.1 * assignment +
            0.7 * test + 0.2 * lab)


# Calculate letter grade of each student
def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"


# Function to calculate the total
# average marks of the whole class
def class_average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
        return get_average(result_list)

    # Student list consisting the


# dictionary of all students
students = [jack, james, dylan, jess, tom]

# Iterate through the students list
# and calculate their respective
# average marks and letter grade
for i in students:
    print(i["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of %s is : %s " % (i["name"],
                                            calculate_total_average(i)))

    print("Letter Grade of %s is : %s" % (i["name"],
                                          assign_letter_grade(calculate_total_average(i))))

    print()

# Calculate the average of whole class
class_av = class_average_is(students)

print("Class Average is %s" % (class_av))
print("Letter Grade of the class is %s "
      % (assign_letter_grade(class_av)))

#
#
#














