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
        print("\tInput the correct information below")
        print("============================================================")

        #name, number, gender, birthdate, email address, City/municipality, Province, Country
        name = input("\tName (First Name Last Name): ")
        number = input("\tNumber (Use 09******286): ")
        gender = input("\tGender (Male, Female, Rather not say): ")
        birthdate = input("\tBirthdate (MM/DD/YYYY): ")
        emailAddress = input("\tEmail Address (sampleemail@gmail.com): ")
        city = input("\tCity/Municipality: ")
        province = input("\tProvince: ")
        country = input("\tCountry: ")
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
        print("\tContact information saved")

    # create choice 2
    elif menu_choice == 2:
        print("============================================================")
        search_name = str(input("\tEnter name of the contact (Last name, First name): "))
        print("============================================================")
        if search_name in contact_tracing:
            for keyInContact_tracing in contact_tracing:
                if search_name == keyInContact_tracing:
                    print(search_name,"'s Contact information")
                    for valueInKeyContact_tracing in contact_tracing[keyInContact_tracing]:
                        print(valueInKeyContact_tracing,": ", contact_tracing[keyInContact_tracing][valueInKeyContact_tracing])
        else:
            print("\tThe contact does not exist")
    # create a looping exit or retry
    print("============================================================")
    program_exit = input("\tDo you want to exit the program? (y/n): ")
    if program_exit.lower() == "y":
        break
    # AMOGUS

