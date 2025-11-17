import os

os.system("cls")

print("STUDENT INFORMATION SYSTEM")
print("=======================================")

students_records = {}

isTrue = True

while isTrue == True:
    print("Select from the options below \nA - Add Personal Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nP - Print All Data\nE - Exit")
    choice = input("Enter your choice ---> ").lower()

    if choice == 'a':
        print("Adding Student Information")
        print(" ------------------------------------ ")
        search_code = input("Enter key for this student ---> ")

        first_name = input("Enter student first name --->").upper()
        last_name = input("Enter student last name ---> ").upper()
        course = input("Enter student course ---> ").upper()
        email = input("Enter student email address ---> ")

        students_records = {search_code : [first_name, last_name, course, email] }
        print("Student data is saved")
        continue
    elif choice == 'b':
        code = input("Enter search code ---> ")

        for j in students_records.keys():
            if code in students_records.keys():
                print("Record Found")
                for i in students_records[code]:
                    print(i)
            else:
                print("No Record Found")
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("Editing Student Record")
        continue
    elif choice == 'e':
        print("Exiting the program...")
        break
    elif choice == 'p':
        pass
        continue
    else:
        print("Invalid Input")
        continue