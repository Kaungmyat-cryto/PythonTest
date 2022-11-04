
profiles = list()


def create_profile(name,age,height,address):
    temp = [name,age,height,address]
    profiles.append(temp)


def show_profile():
    for profile in profiles:
        print("Name: \t%s\nAge: \t%d\nHeight: %.2f\nAddress: %s\n\n" % (profile[0],profile[1],profile[2],profile[3]))


while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    street = input("Enter your street: ")
    township = input("Enter your township: ")

    address = [street,township]

    create_profile(name,age,height,address)

    choice = input('Would you like to add more?(y/n): ')
    if choice == 'y':
        continue
    else:
        show_profile()
        exit(0)
