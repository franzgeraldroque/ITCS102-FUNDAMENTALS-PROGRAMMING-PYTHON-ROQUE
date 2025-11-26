from def_functions import *

print("Welcome to my Finals Project")

name = input("Hi, please input your name --> ")
print(f"Hi, {name}, Welcome to my Compiler Program")

isTrue = True

while isTrue == True:
    print("Pick a Choice: ")
    print("1 - Activities\n2 - CodeChallenges\n0 - Stop The Program")
    choice = input("Enter your choice: ")

#Activities
    if choice == "0":
        print("Stopping the program.")
        break

    elif choice == "1":
        print("Welcome to my Activities Program")
        print("Choose between the given letters: ")
        print("\nA - Activity (1-5)\nB - Activity (6-10)\nC - Activity (11-15)\nD - Activity (16-20)\nE - Activity (21-25)\nF - Activity (26-30)\nS - Stop\nM - Menu")
        act = input("Choose a letter:  ").lower()
        if act == "a":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 1 to 5")
            print("Choose between the given options: ")
            print("a1 - Activity1\na2 - Activity2\na3 - Activity3\na4 - Activity4\na5 - Activity5\n\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a1":
                print(f"You've selected number {act1}")
                print("Welcome to my first python activity")
                activity1()
                continue
            elif act1 == "a2":
                print(f"You've selected number {act1}")
                print("Welcome to my second python activity")
                activity2()
                continue
            elif act1 == "a3":
                print(f"You've selected number {act1}")
                print("Welcome to my third python activity")
                activity3()
                continue
            elif act1 == "a4":
                print(f"You've selected number {act1}")
                print("Welcome to my fourth python activity")
                activity4()
                continue
            elif act1 == "a5":
                print(f"You've selected number {act1}")
                print("Welcome to my fifth python activity")
                activity5()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "b":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 6 to 10")
            print("Choose between the given options: ")
            print("a6 - Activity6\na7 - Activity7\na8 - Activity8\na9 - Activity9\na10 - Activity10\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a6":
                print(f"You've selected number {act1}")
                print("Welcome to my sixth python activity")
                activity6()
                continue
            elif act1 == "a7":
                print(f"You've selected number {act1}")
                print("Welcome to my seventh python activity")
                activity7()
                continue
            elif act1 == "a8":
                print(f"You've selected number {act1}")
                print("Welcome to my eighth python activity")
                activity8()
                continue
            elif act1 == "a9":
                print(f"You've selected number {act1}")
                print("Welcome to my ninth python activity")
                activity9()
                continue
            elif act1 == "a10":
                print(f"You've selected number {act1}")
                print("Welcome to my tenth python activity")
                activity10()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "c":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 11 to 15")
            print("Choose between the given options: ")
            print("a11 - Activity11\na12 - Activity12\na13 - Activity13\na14 - Activity14\na15 - Activity15\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a11":
                print(f"You've selected number {act1}")
                print("Welcome to my eleventh python activity")
                activity11()
                continue
            elif act1 == "a12":
                print(f"You've selected number {act1}")
                print("Welcome to my twelfth python activity")
                activity12()
                continue
            elif act1 == "a13":
                print(f"You've selected number {act1}")
                print("Welcome to my thirteenth python activity")
                activity13()
                continue
            elif act1 == "a14":
                print(f"You've selected number {act1}")
                print("Welcome to my fourteenth python activity")
                activity14()
                continue
            elif act1 == "a15":
                print(f"You've selected number {act1}")
                print("Welcome to my fifteenth python activity")
                activity15()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue
            
        elif act == "d":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 11 to 15")
            print("Choose between the given options: ")
            print("a16 - Activity16\na17 - Activity17\na18 - Activity18\na19 - Activity19\na20 - Activity20\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a16":
                print(f"You've selected number {act1}")
                print("Welcome to my sixteenth python activity")
                activity16()
                continue
            elif act1 == "a17":
                print(f"You've selected number {act1}")
                print("Welcome to my seventeenth python activity")
                activity17()
                continue
            elif act1 == "a18":
                print(f"You've selected number {act1}")
                print("Welcome to my eighteenth python activity")
                activity18()
                continue
            elif act1 == "a19":
                print(f"You've selected number {act1}")
                print("Welcome to my nineteenth python activity")
                activity19()
                continue
            elif act1 == "a20":
                print(f"You've selected number {act1}")
                print("Welcome to my twentieth python activity")
                activity20()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue
        elif act == "e":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 21 to 25")
            print("Choose between the given options: ")
            print("a21 - Activity21\na22 - Activity22\na23 - Activity23\na24 - Activity24\na25 - Activity25\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a21":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-first python activity")
                activity21()
                continue
            elif act1 == "a22":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-second python activity")
                activity22()
                continue
            elif act1 == "a23":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-third python activity")
                activity23()
                continue
            elif act1 == "a24":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-fourth python activity")
                activity24()
                continue
            elif act1 == "a25":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-fifth python activity")
                activity25()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "f":
            print(f"You've selected letter {act}")
            print("Welcome to Activities 26 to 30")
            print("Choose between the given options: ")
            print("a26 - Activity26\na27 - Activity27\na28 - Activity28\na29 - Activity29\na30 - Activity30\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "a26":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-sixth python activity")
                activity26()
                continue
            elif act1 == "a27":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-seventh python activity")
                activity27()
                continue
            elif act1 == "a28":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-eighth python activity")
                activity28()
                continue
            elif act1 == "a29":
                print(f"You've selected number {act1}")
                print("Welcome to my twenty-ninth python activity")
                activity24()
                continue
            elif act1 == "a30":
                print(f"You've selected number {act1}")
                print("Welcome to my thirteeth python activity")
                activity25()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "s": 
            print("Stopping The Program... ")
            break
        elif act == "m": 
            print("Going Back to Menu")
            continue
        else:
            print("Invalid input, choose only between the given choices.")
            continue

#Code Challenges
    if choice == "2":
        print("Welcome to my Code Challenges Program")
        print("Choose between the given letters: ")
        print("\nA - CodeChallenge (1-5)\nB - CodeChallenge (6-10)\nC - CodeChallenge (11-15)\nD - CodeChallenge (16)\nS - Stop\nM - Menu")
        act = input("Choose a letter:  ").lower()
        if act == "a":
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenges 1 to 5")
            print("Choose between the given numbers: ")
            print("c1 - CodeChallenge1\nc2 - CodeChallenge2\nc3 - CodeChallenge3\nc4 - CodeChallenge4\nc5 - CodeChallenge5\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "c1":
                print(f"You've selected number {act1}")
                print("Welcome to my first code challenge")
                codechallenge1()
                continue
            elif act1 == "c2":
                print(f"You've selected number {act1}")
                print("Welcome to my second code challenge")
                codechallenge2()
                continue
            elif act1 == "c3":
                print(f"You've selected number {act1}")
                print("Welcome to my third code challenge")
                codechallenge3()
                continue
            elif act1 == "c4":
                print(f"You've selected number {act1}")
                print("Welcome to my fourth code challenge")
                codechallenge4()
                continue
            elif act1 == "a5":
                print(f"You've selected number {act1}")
                print("Welcome to my fifth code challenge")
                codechallenge5()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue
        elif act == "b": 
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenges 6 to 10")
            print("Choose between the given numbers: ")
            print("c6 - CodeChallenge6\nc7 - CodeChallenge7\nc8 - CodeChallenge8\nc9 - CodeChallenge9\nc10 - CodeChallenge10\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "c6":
                print(f"You've selected number {act1}")
                print("Welcome to my sixth code challenge")
                codechallenge6()
                continue
            elif act1 == "c7":
                print(f"You've selected number {act1}")
                print("Welcome to my seventh code challenge")
                codechallenge7()
                continue
            elif act1 == "c8":
                print(f"You've selected number {act1}")
                print("Welcome to my eighth code challenge")
                codechallenge8()
                continue
            elif act1 == "c9":
                print(f"You've selected number {act1}")
                print("Welcome to my ninth code challenge")
                codechallenge9()
                continue
            elif act1 == "c10":
                print(f"You've selected number {act1}")
                print("Welcome to my tenth codechallenge")
                codechallenge10()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue
        elif act == "c":
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenges 11 to 15")
            print("Choose between the given numbers: ")
            print("c11 - CodeChallenge11\nc12 - CodeChallenge12\nc13 - CodeChallenge13\nc14 - CodeChallenge14\nc15 - CodeChallenge15\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "c11":
                print(f"You've selected number {act1}")
                print("Welcome to my eleventh code challenge")
                codechallenge11()
                continue
            elif act1 == "c12":
                print(f"You've selected number {act1}")
                print("Welcome to my twelfth code challenge")
                codechallenge12()
                continue
            elif act1 == "c13":
                print(f"You've selected number {act1}")
                print("Welcome to my thirteenth code challenge")
                codechallenge13()
                continue
            elif act1 == "c14":
                print(f"You've selected number {act1}")
                print("Welcome to my fourteenth code challenge")
                codechallenge14()
                continue
            elif act1 == "c15":
                print(f"You've selected number {act1}")
                print("Welcome to my fifteenth codechallenge")
                codechallenge15()
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "d":
            print(f"You've selected letter {act}")
            print("Welcome to Code Challenge 16")
            print("Choose between the given numbers: ")
            print("c16 - CodeChallenge16\nM - Menu")
            act1 = input("Choose a number:  ").lower()
            if act1 == "c16":
                print(f"You've selected number {act1}")
                print("Welcome to my sixteenth code challenge")
                codechallenge16()
                continue
            # elif act1 == "c12":
            #     print(f"You've selected number {act1}")
            #     print("Welcome to my twelfth code challenge")
            #     codechallenge12()
            #     continue
            # elif act1 == "c13":
            #     print(f"You've selected number {act1}")
            #     print("Welcome to my thirteenth code challenge")
            #     codechallenge13()
            #     continue
            # elif act1 == "c14":
            #     print(f"You've selected number {act1}")
            #     print("Welcome to my fourteenth code challenge")
            #     codechallenge14()
            #     continue
            # elif act1 == "c15":
            #     print(f"You've selected number {act1}")
            #     print("Welcome to my fifteenth codechallenge")
            #     codechallenge15()
            #     continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "s": 
            print("Stopping The Program... ")
            break
        elif act == "m": 
            print("Going Back to Menu")
            continue
        else:
            print("Invalid input, choose only between the given choices.")
            continue
