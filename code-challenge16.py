import os
import json

os.system("cls")

print("STUDENT INFORMATION SYSTEM")
print("=======================================")

students_records = {}

isTrue = True

while isTrue == True:
    print("Select from the options below \nA - Add Student Record\nB - Print all Record\nC - Search Student Record\nD - Delete a Student Record\nE - Edit Student Record\nF - Export Data\nG - Import Data\nH - Exit ")
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
                break
        continue
    elif choice == 'd':
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
                students_records.pop(search_id)
                print("Record is deleted")
            else:
                print("No record found")
                break
        continue
    elif choice == 'e':
        os.system()
        print("Edit / modify a Student Record")

        search_id = input("Input Student ID to Search ---> ").lower()

        for id in students_records.keys():
            if search_id in students_records.keys():
                print("Record is found")
                #print the record search student
                for i in students_records[search_id]:
                    print(f' -- {i}')
                
                first_name = input("Enter new student first name --->").upper()
                last_name = input("Enter new student last name ---> ").upper()
                course = input("Enter new student course ---> ").upper()
                email = input("Enter new student email address ---> ")

                students_records[search_id] = first_name
                students_records[search_id] = last_name
                students_records[search_id] = course
                students_records[search_id] = email

                print("Data Updated")
            else:
                print("No record found")
                break
        continue
        
    elif choice == 'f':
        os.system("cls")
        print("Export Data")
        # file name, read / write
        with open("student_records.json", 'w') as new_file:
            json.dump(students_records, new_file, indent=4)
        
        print("Data Exported")
        continue
    elif choice == 'g':
        os.system("cls")
        print("Import Data")
                # file name, read / write
        with open("student_records.json", 'r') as new_file:
            student_json = json.load(new_file)

        students_records = student_json
        print("Data Imported")
        continue
    elif choice == 'h':
        print("Exiting the program.....")
        break
    else:
        print("Invalid Input")
        continue
