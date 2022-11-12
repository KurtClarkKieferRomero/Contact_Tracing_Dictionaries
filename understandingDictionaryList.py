# Introduce the program
print("============================================================")
print("\tWelcome to Contract Tracing program")
print("============================================================")
print("\tListed below is the menu of the program")
print("============================================================")

# Create a menu
print("\tPlease Enter only numbers")
print("\t1. Add Contacts")
print("\t2. Search Contacts")
print("\t3. Exit")
print("============================================================")

# Create empty dictioanry

# Ask for the user input
menu_choice = int(input("\tWhat is your choice? "))

#Create empty dictionary
contact_tracing = {}

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

    # Created empty dictionary inside contact_tracing dictionary
    contact_tracing[name] = {}
    contact_tracing[name]["contactName"] = name
    contact_tracing[name]["contactNumber"] = number
    contact_tracing[name]["contactGender"] = gender
    contact_tracing[name]["contactBirthdate"] = birthdate
    contact_tracing[name]["contactEmailAddress"] = emailAddress
    contact_tracing[name]["contactCity"] = city
    contact_tracing[name]["contactProvince"] = province
    contact_tracing[name]["contactCountry"] = country

# create choice 2
# create a looping exit or retry
# AMOGUS

