# Create empty dictionary
contact_tracing = {}
# Introduce the program
print("============================================================")
print("\tWelcome to Contract Tracing program")
print("============================================================")
print("\tListed below is the menu of the program")

while True:
    # Create a menu
    print("============================================================")
    print("\tPlease Enter only numbers")
    print("\t1. Add Contacts")
    print("\t2. Search Contacts")
    print("\t3. Exit")
    print("============================================================")

    # Ask for the user input
    menu_choice = int(input("\tWhat is your choice? "))

    #Create empty dictionary


    # Establish the choices in the menu
    # create choice 1

    if menu_choice == 1:
        print("============================================================")
        print("Input the correct information below")
        print("============================================================")

        #name, number, gender, birthdate, email address, City/municipality, Province, Country
        name = input("Name (Last name, First Name): ")
        number = input("Number (Use 09******286 format): ")
        gender = input("Gender (Male, Female, Rather not say): ")
        birthdate = input("Birthdate (MM/DD/YYYY): ")
        emailAddress = input("Email Address (sampleemail@gmail.com): ")
        city = input("City/Municipality: ")
        province = input("Province: ")
        country = input("Country: ")
        contact_tracing[name] = {}
        contact_tracing[name]["Contact Name"] = name
        contact_tracing[name]["Contact Number"] = number
        contact_tracing[name]["Contact Gender"] = gender
        contact_tracing[name]["Contact Birthdate"] = birthdate
        contact_tracing[name]["Contact EmailAddress"] = emailAddress
        contact_tracing[name]["Contact City"] = city
        contact_tracing[name]["Contact Province"] = province
        contact_tracing[name]["Contact Country"] = country
        print("============================================================")
        print("Contact information saved")

    # create choice 2
    elif menu_choice == 2:
        search_name = str(input("Enter name of the contact (Last name, First name): "))
        if search_name in contact_tracing:
            for keyInContact_tracing in contact_tracing:
                if search_name == keyInContact_tracing:
                    print(search_name,": Contact information")
                    for valueInKeyContact_tracing in contact_tracing[keyInContact_tracing]:
                        print(valueInKeyContact_tracing,": ", contact_tracing[keyInContact_tracing][valueInKeyContact_tracing])
        else:
            print("The contact does not exist")
    # create a looping exit or retry
    print("============================================================")
    program_exit = input("Do you want to exit the program? (y/n): ")
    if program_exit.lower() == "y":
        break
    # AMOGUS

