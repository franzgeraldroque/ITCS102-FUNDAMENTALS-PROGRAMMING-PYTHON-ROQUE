import os

os.system("cls")

print("STUDENT INFORMATION SYSTEM")
print("=======================================")

students_records = {}

isTrue = True

while isTrue == True:
    print("Select from the options below \nA - Add Student Record\nB - Print all Record\nC - Search Student Record\nD - Delete a Student Record\nE - Edit Student Record\nF - Export Data\nG - Exit")
    choice = input("Enter your choice ---> ").lower()

    if choice == 'a':
        os.system("cls")
        print("Adding Student Information")
        print(" ------------------------------------ ")
        student_id = input("Enter key for this student ---> ")

        first_name = input("Enter student first name --->").upper()
        last_name = input("Enter student last name ---> ").upper()
        course = input("Enter student course ---> ").upper()
        email = input("Enter student email address ---> ")

        students_records[student_id] = [first_name, last_name, course, email]
        print("Student data is saved")
        continue
    elif choice == 'b':
        os.system("cls")
        print("Printing Student Record")

        for id, record in students_records.items():
            print(f'Student ID {id} in Student Record {record}')
        continue
    elif choice == 'c':
        os.system("cls")
        print("Search for Student Record")
        print("================================")

        search_id = input("Input Student ID to Search ---> ").lower()
        for id in students_records.keys():
            if search_id in students_records.keys():
                print("Record is found")
                #print the record search student
                for i in students_records[search_id]:
                    print(f' -- {i}')
            else:
                print("No record found")
        continue
    elif choice == 'd':
        os.system("cls")
        print("Delete a Existing Record")

        search_id = input("Input Student ID to Search ---> ").lower()
        for id in students_records.keys():
            if search_id in students_records.keys():
                print("Record is found")
                #print the record search student
                for i in students_records[search_id]:
                    print(f' -- {i}')
                students_records.pop(search_id)
                print("Record is deleted")
            else:
                print("No record found")
        continue
    elif choice == 'e':
        # print("Edit a Student Record")

        # edit = input("Choose a student to edit")
        # for e in students_records.items():
        #     if edit in students_records.keys():
        #         for 

        pass
        continue
    elif choice == 'f':
        print("Export Data")
        pass
        continue
    elif choice == 'g':
        print("Exiting the program.....")
        break
    else:
        print("Invalid Input")
        continue
