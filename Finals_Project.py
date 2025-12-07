from def_function import *
import os

print("=============================================")
print("\n\tWelcome to my Finals Project\n")
print("=============================================")

name = input("\nHi, please input your name --> ").capitalize()
print("=============================================")
print(f"\nHi, {name}, Welcome to my Compiler Program\n")


isTrue = True

while isTrue == True:
    print("---------------------------------------------")
    print("\nPick a Choice: ")
    print("\t1 - Activities\n\t2 - CodeChallenges\n\t0 - Stop The Program")
    print("---------------------------------------------")
    choice = input("\nEnter your choice: ")

#Activities
    if choice == "0":
        print("Stopping the program.")
        break

    elif choice == "1":
        os.system("cls")
        print("---------------------------------------------")
        print("\n\tWelcome to my Activities Program\n")
        
        print("\nChoose between the given letters: \n")
        print("---------------------------------------------")
        print("\n\tA - Activity (1-5)\n\tB - Activity (6-10)\n\tC - Activity (11-15)\n\tD - Activity (16-20)\n\tE - Activity (21-25)\n\tF - Activity (26-28)\n\tS - Stop\n\tM - Menu\n")
        print("---------------------------------------------")
        act = input("Choose a letter:  ").upper()
        
        if act == "A":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 1 to 5\n")
            print("Choose between the given options: ")
            print("\ta1 - Activity1\n\ta2 - Activity2\n\ta3 - Activity3\n\ta4 - Activity4\n\ta5 - Activity5\n\t\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a1":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my first python activity\n")

                print("This activity contains a basic output.")
                print("\nIt prints a simple, fixed greeting message to the console.")
                print("\n---------------------------------------------\n")
                print("INPUT: \nprint('Hello Hanniel my BFF')\n")
                print("OUTPUT: ")
                activity1()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a2":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my second python activity\n")

                print("This activity contains input/output and variables")
                print("\nIt prompts the user for their name using input(), stores it in a variable, and then prints a personalized greeting.")
                print("\n---------------------------------------------\n")
                print("INPUT: \nname = input('What is your name .?\nprint('Hello', name, 'Welcome to the Matrix')\n")
                print("OUTPUT: ")
                activity2()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a3":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my third python activity\n")

                print("This activity contains string formatting")
                print("\nIt demonstrates the use of special characters like the newline ('\\n') and tab ('\\t') escape sequences to format and space out the printed text.")
                print("\n---------------------------------------------\n")
                print("INPUT: \nprint('Happy\n\tMonday,')\nprint('BSIT 1A\n\t from DLL')\nprint('Hi ex, \n\t kakalimutan na kita')\nprint('The quick snatcher runs\n\t over\n\t manila city')\n")
                print("OUTPUT: ")
                activity3()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a4":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fourth python activity\n")

                print("This activity contains string length")
                print("\nIt takes a string input from the user and uses the built-in len() function to calculate and print the total number of characters in the string.")
                print("\n---------------------------------------------\n")
                print("INPUT: \nname = input('Enter a string -> ')\nprint('Your name has ', len(name), 'character')\n")
                print("OUTPUT: ")
                activity4()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a5":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fifth python activity\n")

                print("This activity contains data types and eval()")
                print("\nIt takes input, uses eval() to execute the input as Python code (determining its type), and then uses the type() function to print its data type before performing an addition operation.\nNote: eval() is generally considered unsafe for untrusted input.")
                print("\n---------------------------------------------\n")
                print("INPUT: \nsomething = eval(input('Input something --> '))\nprint('The data type of something is',type(something))\nanswer = 5 + something\nprint('The answer is ', answer)\n")
                print("OUTPUT: ")
                activity5()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "B":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 6 to 10\n")
            print("\nChoose between the given options: \n")
            print("\ta6 - Activity6\n\ta7 - Activity7\n\ta8 - Activity8\n\ta9 - Activity9\n\ta10 - Activity10\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a6":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my sixth python activity\n")

                print("This activity contains arithmetic operators")
                print("\nIt prompts for two numbers and performs all major arithmetic operations (addition +, subtraction -, multiplication *, division /, exponentiation **, modulus %, and floor division //).")
                print("\n---------------------------------------------\n")
                print("INPUT: \nn1 = eval(input('Enter the first number : '))\nn2 = eval(input('Enter the second number : '))\ns = n1 + n2\nd = n1 - n2\np = n1 * n2\nq = n1 / n2\nprint ('\\nThe sum of',n1, 'and' ,n2, 'is',s)\nprint ('The difference of',n1, 'and' ,n2, 'is' ,d)\nprint('The product of',n1, 'and' ,n2, 'is' , p)\nprint ('The quotient of',n1, 'and',n2, 'is', q)\nprint(n1, 'exponent by',n2, 'is', n1**n2)\nprint ('The remainder of',n1, 'and' , n2, 'is', n1 % n2)\nprint('The floor division of',n1, 'and' ,n2, 'is' ,n1//n2)\n")
                print("OUTPUT: ")
                activity6()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a7":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my seventh python activity\n")

                print("This activity contains assignment operators")
                print("\nIt demonstrates the use of compound assignment operators like += (add and assign) and *= (multiply and assign) to modify the value of the variable f.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nf = 7\nprint("the value of a is ", f)\nf += 17\nf = 3\nf *= 2\nf = 6\nprint("the value of a is ", f)\n')
                print('OUTPUT: ')
                activity7()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a8":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my eighth python activity\n")

                print("This activity contains comparison operators")
                print("\nIt shows how comparison operators (>, !=) work to compare two values, resulting in a Boolean output (True or False).")
                print("\n---------------------------------------------\n")
                print('INPUT: \nex = 18\nako = 18\nprint(ex > ako)\nbirthday1 = 3\nbirthday2 = 17\nprint(birthday1 != birthday2)\n')
                print('OUTPUT: ')
                activity8()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a9":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my ninth python activity\n")

                print("This activity contains logical operators")
                print("\nIt uses logical operators (or, not) to combine or negate Boolean expressions, determining the final True or False outcome based on the state of variables valorant and sleep.")
                print("\n---------------------------------------------\n")
                print("INPUT: #valorant = 'stress'\nvalorant = 'joy'\nsleep = 'rest'\nprint((valorant == 'stress') or (sleep == 'rest'))\nprint(not((valorant == 'stress') or (sleep == 'rest')))\n")
                print("OUTPUT: ")
                activity9()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a10":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my tenth python activity\n")

                print("This activity contains If-Else (simple conditional)")
                print("\nIt implements a simple conditional logic (if/else). It checks if a user is a student to determine if they qualify for a 20 percent fare discount.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#tricycle fare\nname = input("Input your name ---> ")\nisStudent = input("Are you a student (Yes / No) --> ")\nfare = eval(input("bayad --> "))\nif isStudent.lower() == "yes":\n\tdiscount = fare * .20\n\tnew_fare = fare - discount\n\tprint("Hi", name, " student discount is ", discount, " Discounted fare is ", new_fare)\nelse:\n\tprint("Sorry", name, " you are not eligible for student discount")\n')
                print('OUTPUT: ')
                activity10()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "C":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 11 to 15\n")
            print("\nChoose between the given options: \n")
            print("\ta11 - Activity11\n\ta12 - Activity12\n\ta13 - Activity13\n\ta14 - Activity14\n\ta15 - Activity15\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a11":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my eleventh python activity\n")

                print("This activity contains If-Elif-Else (multiple conditionals)")
                print("\nIt uses an if-elif-else structure to evaluate multiple conditions based on a temperature input, categorizing the temperature (e.g., cold, warm, hot).")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#1 to 20 cold\n#21 to 30 luke warm\n#31 to 40 warm\n#41 to 50 hot\n#51 and above boiling point\ntemp = eval(input("Enter temperature --> "))\nif temp >= 1 and temp <= 20:\n\tprint("Temperature outside is cold")\nelif temp >= 21 and temp <= 30:\n\tprint("Temperature outside is luke warm")\nelif temp >= 31 and temp <= 40:\n\tprint("Temperature outside is warm")\nelif temp >= 41 and temp <= 50:\n\tprint("Temperature outside is hot")\nelif temp >= 51:\n\tprint("Temperature outside is super duper hot")\nelse:\n\tprint("Invalid temperature")\n')
                print('OUTPUT: ')
                activity11()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a12":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twelfth python activity\n")

                print("This activity contains For Loop (Range, Step)")
                print("\nIt uses a for loop with the range(start, stop, step) function to iterate and print a sequence of numbers (starting from 1, up to 99, stepping by 2), alongside a fixed message.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#print("Hello World")\n#name = input("Enter your name: ")\n#print("Hello", name, "say Hi to your future girlfriend")\n#print hello world 10 times\nfor truepa in range(1, 100, 2):\n\tprint(truepa, "- kamusta sa aking magiting na kaibigan")\n')
                print('OUTPUT: ')
                activity12()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a13":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my thirteenth python activity\n")

                print("This activity contains For Loop (Accumulator)")
                print("\nIt uses a for loop to repeatedly prompt the user for 10 numbers. It uses an accumulator variable (num) to calculate and display the running and final sum of the inputs.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#using for loop, ask user to input 10 numbers\n#after input, get the summation of all the numbers\nnum = 0\nfor cashg in range(1, 11):\n\tnumber = eval(input("Enter a number --> "))\n\tnum += number\n\tprint("ang laman ng imong gcash ay",num)\nprint("ang imong gcash ay may laman na",num, "pidi ba akong makikurot kahit pang lud lang")\n')
                print("OUTPUT: ")
                activity13()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a14":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fourteenth python activity\n")

                print("This activity contains For Loop (Descending)")
                print("\nIt uses a for loop with a negative step value in range(20, 0, -1) to print numbers in descending order (from 20 down to 1).")
                print("\n---------------------------------------------\n")
                print("INPUT: \n#descending numbers\nfor aports in range(20, 0, -1):\nprint(aports)\n")
                print("OUTPUT: ")
                activity14()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a15":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fifteenth python activity\n")

                print("This activity contains For Loop & Conditional Logic")
                print("\nIt iterates 10 times to take numeric input. It uses an if condition (num % 2 == 1) to check if the number is odd and only adds odd numbers to an accumulating sum.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#print("ODD NUMBER SUMMATION")\n#print("INPUT 10 ODD NUMBERS")\nodd_sum = 0\nfor i in range(1,11,1):\n\tnum = eval(input("Enter a number -->"))\n\tif num % 2 == 1:\n\t\todd_sum += num\nprint(f"The sum of all odd number is: {"odd_sum"}")\n')
                print("OUTPUT: ")
                activity15()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue
            
        elif act == "D":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 11 to 15\n")
            print("\nChoose between the given options: \n")
            print("\ta16 - Activity16\n\ta17 - Activity17\n\ta18 - Activity18\n\ta19 - Activity19\n\ta20 - Activity20\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a16":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my sixteenth python activity\n")

                print("This activity contains For Loop & end Parameter")
                print("\nIt uses a for loop to print numbers from 1 to 10. The end= ',' parameter in the print() function makes the numbers print on a single line, separated by a comma and a space.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#print("Print numbers 1 to 10 horizontally")\nfor i in range(1,11,1):\n\tprint(i,end=", ")\n')
                print("OUTPUT: ")
                activity16()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a17":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my seventeenth python activity\n")

                print("This activity contains Nested For Loop (Rectangle)")
                print("\nIt uses a nested for loop structure (a loop inside a loop) to print a 10 x 10 block of numbers, forming a basic rectangle pattern.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfor i in range(1, 11, 1):\n\tfor x in range(1, 11, 1):\n\t\tprint(x, end=" ")\n\tprint()\n')
                print("OUTPUT: ")
                activity17()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a18":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my eighteenth python activity\n")

                print("This activity contains Nested For Loop (Right Triangle of Numbers)")
                print("\nIt uses a nested loop where the inner loop's range depends on the outer loop's index (i) to print an ascending right-angle triangle pattern of numbers.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfor i in range(1, 11, 1):\n\tfor x in range(1, i, 1):\n\t\tprint(x, end=" ")\n\tprint()\n')
                print("OUTPUT: ")
                activity18()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a19":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my nineteenth python activity\n")

                print("This contains Nested For Loop (Right Triangle of Stars)")
                print("\nIt is similar to Activity 18, this creates an ascending right-angle triangle pattern, but it uses the character * instead of numbers.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfor i in range(1, 11, 1):\nfor x in range(1, i, 1):\n\t\tprint("*", end=" ")\n\tprint()\n')
                print("OUTPUT: ")
                activity19()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a20":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twentieth python activity\n")

                print("This contains Nested For Loop (Inverted Triangle)")
                print("\nIt uses two sets of nested for loops (one for printing spaces and one for printing stars) to create an inverted right-angle triangle pattern of stars.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfor i in range(1, 11, 1):\nfor x in range(1, i, 1):\n\t\tprint(" ", end=" ")\n\tfor f in range(10, i, -1):\n\t\tprint("*", end=" ")\n\tprint()\n')
                print("OUTPUT: ")
                activity20()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "E":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 21 to 25\n")
            print("\nChoose between the given options: \n")
            print("\ta21 - Activity21\n\ta22 - Activity22\n\ta23 - Activity23\n\ta24 - Activity24\n\ta25 - Activity25\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a21":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-first python activity\n")

                print("This activity contains While Loop, break, and continue")
                print("\nIt implements a while loop that continues as long as isDirty is True. It demonstrates break to exit the loop entirely and continue to skip the rest of the current iteration and start the next one.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nisDirty = True\nwhile isDirty == True:\n\tconfirm = input("Gusto mo bang magpatuloy pa sa paglalaba? (tara / ayaw ko)-->").lower()\n\tif confirm == "tara":\n\t\tprint("Tayoy magpapatuloy")\n\t\tcontinue\n\telif confirm == "ayaw ko":\n\t\tprint("Itigil na natin to!!")\n\t\tbreak\n\telse:\n\t\tprint("Wala ka naman sa tama eh")\n\t\tcontinue\n')
                print("OUTPUT: ")
                activity21()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a22":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-second python activity\n")

                print("This activity contains While Loop (Guessing Game)")
                print("\nIt creates a simple 'Guess the Number' game using a while loop that continues until the user's guess matches a randomly generated number, tracking the number of tries.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nimport random\nnum = random.randint(1,10)\ntries = 0\nistrue = True\nwhile istrue == True:\n\tguesser = eval(input("Guess a number between 1-10: "))\n\ttries += 1\n\tif guesser == num:\n\t\tprint("Congratulations")\n\t\tprint(f"The number is {"num"}")\n\t\tprint(f"You only took {"tries"} tries")\n\t\tbreak\n\telse:\n\t\tprint("The number you picked is invalid, please continue...")\n\t\tcontinue\n')
                print("OUTPUT: ")
                activity22()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a23":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-third python activity\n")

                print("This activity contains Lists, Strings, and Iteration")
                print("\nIt demonstrates fundamental List methods like append(), pop(), and insert(). It also shows how to iterate over both a list and a string, including string slicing ([::-1]) to print a string in reverse.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nnm = ["apple","hotdog","orange","watermelon","egg"]\nnm.append("mango")   #add an item to the last of the list\nprint(nm)\nnm.pop()    #remove the last item\nprint(nm)\nnm.insert(0,"watermelon")   #add item in dif position\nprint(nm)\nfor i in nm:\n\tprint(f"{"i"}  in the basket")    #all fruits one by one with "in the basket" at the last\nmi = "Franz Gerald L. Roque"\nfor u in mi:\n\tprint(u)    #Will print my name from f to e\nprint("\nReversed\n")\nfor q in mi[::-1]:  #will print my name in reverse from n to j\n\tprint(q)\n')
                print("OUTPUT: ")
                activity23()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a24":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-fourth python activity\n")

                print("This activity contains User-Defined Functions (Parameters)")
                print("\nIt defines and calls two reusable functions: greeter(name) which takes a string parameter and prints a greeting, and summation(x) which takes a numeric parameter and calculates the sum of all integers from x down to 1.")
                print("\n---------------------------------------------\n")
                print('INPUT: \ndef greeter(name):\n\tprint(f"Hi {"name"}, kamusta ka na?")\ndef summation(x):\n\tsum = 0\n\tfor i in range (x,0,-1):\n\t\tsum += i\n\tprint(f"The sum of {"x"} is {"sum"}")\ngreeter("Franz")\ngreeter("Gerald")\ngreeter("Roque")\nsummation(18)\nsummation(11)\n')
                print("OUTPUT: ")
                activity24()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a25":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-fifth python activity\n")

                print("This activity contains Program Menu & Function Calls")
                print("\nIt creates a main program menu using a while loop and if-elif-else statements. The user's choice then calls one of the previously defined activities (activity1 to activity4), effectively creating a multi-function program.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfrom activity25_1 import *\nname = input("Hi, What is your name? --> ")\nprint(f"Welcome {"name"}, to my compuler program ")\nisContinue = True\nwhile isContinue == True:\n\tprint("Select a program")\n\tprint("A - Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nE - Exit")\n\tchoose = input("What program / code would you like to run --> ").lower()\n\tif choose == "a":\n\t\tactivity1()\n\t\tcontinue\n\telif choose == "b":\n\t\tactivity2()\n\t\tcontinue\n\telif choose == "c":\n\t\tactivity3()\n\t\tcontinue\n\telif choose == "d":\n\t\tactivity4()\n\t\tcontinue\n\telif choose == "e":\n\t\tprint("Exiting the system")\n\t\tbreak\n\telse:\n\t\tprint("Error, please only select the given choices")\n')
                print("OUTPUT: ")
                activity25()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "F":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Activities 26 to 28\n")
            print("\nChoose between the given options: \n")
            print("\ta26 - Activity26\n\ta27 - Activity27\n\ta28 - Activity28\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "a26":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-sixth python activity\n")

                print("This activity contains Dictionaries")
                print("\nIt creates a basic dictionary (Language) to store key-value pairs (Language: Phrase). It demonstrates iterating over the dictionary's items (.items()) and accessing a specific value using a user-provided key.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#Create a dictionary\nLanguage = {"Filipino": "kumain ka na?", "Englisn": "did you ate?", "Spanish": "has comido?", "French": "as-tu mangé", "Japanese": "食べましたか"}\nprint("Nagkaon ka na?")\nprint("\nKumain ka na? in every language")\nfor i,x in Language.items():\n\tprint(f"\tLanguage for kumain ka na? --> {"i"}")\nkaon = input("Pick only one language: \n").capitalize()\nprint({"Language[kaon]"})\n')
                print("OUTPUT: ")
                activity26()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a27":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-seventh python activity\n")

                print("This activity contains Interactive Dictionary Program")
                print("\nIt implements a more complex, interactive menu system for a dictionary (empty_directory). It allows the user to add key-value pairs, print all items, search for a value by its key, and exit the loop, demonstrating practical dictionary manipulation within a while loop.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nprint("Adding Data to directory")\nprint("=========================================")\ngo_lang = True\nempty_directory = {""}\n#if printing values .values()\n#if printing both the values and items .items()\ndef anim_print():\n\tfor i,j in empty_directory.items():\n\t\tprint(f"Key - {"i"}, Title - {"j"}")\ndef forsearch(search_key):\n\tprint("Searching ...")\n\tif search_key in empty_directory:\n\t\tprint(f"Result shows {empty_directory[search_key].upper()} in our database")\n\telse:\n\t\tprint("No results found for that key.")\nwhile go_lang == True:\n\tkey = input("Input keys for this anime ---> ")\n\tanim = input("Enter the anime title ---> ")\n\tempty_directory[key] = anim\n\tchoice = input("Would you like to continue adding anime: \ny - Yes\nn - No\np - Print\ns - Search:\n ").lower()\n\tif choice == "y":\n\t\tprint("Continuing ... ")\n\t\tcontinue\n\telif choice == "p":\n\t\tanim_print()\n\t\tcontinue\n\telif choice == "s":\n\tcode = input("Enter the code of the anime: ")\n\t\tforsearch(code)\n\telif choice == "n":\n\t\tprint("Stopping the program ...")\n\t\tbreak\n\telse:\n\t\tprint("Error, pick between the choices only")\n')
                print("OUTPUT: ")
                activity27()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "a28":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twenty-eighth python activity\n")

                print("This activity contains External Libraries (Pygame)")
                print("It can only function inside a virtual environment")
                print("\nIt This is a complete, multi-step program that uses the Pygame library to create a functional Snake Game. It initializes the game, handles movement/input, draws the snake and food, checks for collisions, and manages the game loop.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n#Step 1\nimport pygame\nimport time\nimport random\n# Initialize Pygame\npygame.init()\n# Screen size\nwidth = 600\nheight = 400\nscreen = pygame.display.set_mode((width, height))\npygame.display.set_caption("Snake Game")\n# Colors (RGB)\nwhite = (255, 255, 255)\nblack = (0, 0, 0)\nred = (213, 50, 80)\ngreen = (0, 255, 0)\n# Game speed and block size\nclock = pygame.time.Clock()\nspeed = 10\nsnake_block = 10\n# Font for messages\nfont_style = pygame.font.SysFont(None, 30)\n#Step 2\n def draw_snake(snake_list):\n\tfor block in snake_list:\n\t\tpygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])\n#Step 3 \ndef game_loop():\n\tgame_over = False\n\tgame_close = False\n\t# Starting position of the snake\n\tx = width / 2\n\ty = height / 2\n\tx_change = 0\n\ty_change = 0\n\tsnake_list = []\n\tlength_of_snake = 1\n\t# Generate first food\n\tfood_x = round(random.randrange(0, width - snake_block) / 10) * 10\n\tfood_y = round(random.randrange(0, height - snake_block) / 10) * 10\n\twhile not game_over:\n\t\t# Loss screen\n\t\twhile game_close:\n\t\t\tscreen.fill(black)\n\t\t\tmessage = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)\n\t\t\tscreen.blit(message, [width / 6, height / 3])\n\t\t\tpygame.display.update()\n\t\t\tfor event in pygame.event.get():\n\t\t\t\tif event.type == pygame.KEYDOWN:\n\t\t\t\t\tif event.key == pygame.K_q:\n\t\t\t\t\tgame_over = True\n\t\t\t\t\tgame_close = False\n\t\t\t\t\telif event.key == pygame.K_c:\n\t\t\t\t\tgame_loop()\n\t\t# Event handling (keyboard)\n\t\t\for event in pygame.event.get():\n\t\t\tif event.type == pygame.QUIT:\n\t\t\t\tgame_over = True\n\t\t\tif event.type == pygame.KEYDOWN:\n\t\t\t\tif event.key == pygame.K_LEFT:\n\t\t\t\t\tx_change = -snake_block\n\t\t\t\t\ty_change = 0\n\t\t\t\telif event.key == pygame.K_RIGHT:\n\t\t\t\t\tx_change = snake_block\n\t\t\t\t\ty_change = 0\n\t\t\t\telif event.key == pygame.K_UP:\n\t\t\t\t\ty_change = -snake_block\n\t\t\t\t\tx_change = 0\n\t\t\t\telif event.key == pygame.K_DOWN:\n\t\t\t\t\ty_change = snake_block\n\t\t\t\t\tx_change = 0\n\t\t# Check if snake hits the wall\n\t\tif x >= width or x < 0 or y >= height or y < 0:\n\t\t\tgame_close = True\n\t\t# Update position\n\t\tx += x_change\n\t\ty += y_change\n\t\t# Draw background and food\n\t\tscreen.fill(black)\n\t\tpygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])\n\t\t# Add snake head\n\t\tsnake_head = [x, y]\n\t\tsnake_list.append(snake_head)\n\t\t# Remove extra segments if not growing\n\t\tif len(snake_list) > length_of_snake:\n\t\t\tdel snake_list[0]\n\t\t# Check self-collision\n\t\tfor segment in snake_list[:-1]:\n\t\t\tif segment == snake_head:\n\t\t\t\tgame_close = True\n\t\t# Draw the snake\n\t\tdraw_snake(snake_list)\n\t\t# Update display\n\t\tpygame.display.update()\n\t\t# Check if snake eats food\n\t\tif x == food_x and y == food_y:\n\t\t\tfood_x = round(random.randrange(0, width - snake_block) / 10) * 10\n\t\t\tfood_y = round(random.randrange(0, height - snake_block) / 10) * 10\n\t\t\tlength_of_snake += 1\n\t\t# Control game speed\n\t\tclock.tick(speed)\n\t# Quit Pygame\n\tpygame.quit()\n\tquit()\n# Start the game\ngame_loop()\n')
                print("OUTPUT: ")
                activity28()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
            else:
                print("Invalid input, try again")
                continue

        elif act == "S": 
            print("Stopping The Program... ")
            break
        elif act == "M": 
            os.system("cls")
            print("Going Back to Menu")
            continue
        else:
            os.system("cls")
            print("Invalid input, choose only between the given choices.")
            continue

#Code Challenges
    elif choice == "2":
        os.system("cls")
        print("---------------------------------------------")
        print("\n\tWelcome to my Code Challenges Program\n")
        
        print("\nChoose between the given letters: \n")
        print("---------------------------------------------")
        print("\n\tA - CodeChallenge (1-5)\n\tB - CodeChallenge (6-10)\n\tC - CodeChallenge (11-16)\n\tS - Stop\n\tM - Menu\n")
        print("---------------------------------------------")
        act = input("Choose a letter:  ").upper()

        if act == "A":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Code Challenges 1 to 5\n")
            print("\nChoose between the given options: \n")
            print("\tc1 - CodeChallenge1\n\tc2 - CodeChallenge2\n\tc3 - CodeChallenge3\n\tc4 - CodeChallenge4\n\tc5 - CodeChallenge5\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "c1":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my first code challenge\n")

                print("This code challenge contains Advanced String Formatting (Visual Art)")
                print("\nIt uses extensive newlines (\n) and tabs (\t) to draw a large, diamond-shaped text-based art pattern (ASCII art) to the console, incorporating the user's name in the center.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge1()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c2":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my second code challenge\n")

                print("This code challenge contains Greedy Algorithm (Denominations)")
                print("\nIt implements a greedy approach to break down a monetary amount into the largest possible number of Philippine peso denominations (1000, 500, 200...). It uses integer division (//) and modulus (%) to count bills and calculate the remaining amount.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge2()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c3":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my third code challenge\t")

                print("This code challenge contains Security (Hidden Input) & String Comparison")
                print("\nIt uses the getpass module for hidden password input (security) and employs logical and to check if both the username and password match the stored credentials for access control.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge3()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c4":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fourth code challenge\n")

                print("This code challenge contains Conditional Logic (Even/Odd)")
                print("\nIt takes a numeric input and uses the modulus operator (%) to check for a remainder of zero when divided by 2 (number % 2 == 0). This determines if the number is even or odd.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge4()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c5":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fifth code challenge\n")

                print("This code challenge contains Nested Conditionals (Recommender System)")
                print("\nIt creates a basic Anime Recommender System using heavily nested if-elif-else statements. It processes input for genre, time, and decade to provide a recommendation based on specific combinations of choices.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge5()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "B":
            os.system("cls") 
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Code Challenges 6 to 10\n")
            print("\nChoose between the given options: \n")
            print("\tc6 - CodeChallenge6\n\tc7 - CodeChallenge7\n\tc8 - CodeChallenge8\n\tc9 - CodeChallenge9\n\tc10 - CodeChallenge10\n\tm - Menu\n")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "c6":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my sixth code challenge\n")

                print("This code challenge contains Loop (Factorial Calculation)")
                print("\nIt calculates the factorial of a user-inputted number. It uses a for loop that iterates backward to compute the product of all positive integers less than or equal to the number, showing the step-by-step calculation.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge6()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c7":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my seventh code challenge\n")

                print("This code challenge contains Loop (Input Validation & Conditional Sum)")
                print("\nIt uses a for loop to repeatedly ask for input. It implements an if-else check within the loop to validate if the number is odd; if it's odd, it is added to the sum; otherwise, the user is notified.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge7()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c8":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my eighth code challenge\n")

                print("This code challenge contains Loop (Multiplication Table)")
                print("\nIt takes a number from the user and uses a for loop to generate and display its multiplication table from 1 up to 10.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge8()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c9":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my ninth code challenge\n")

                print("This code challenge contains Loop & Time Module (Countdown Timer)")
                print("\nIt imports the time module and uses a for loop to iterate backward from a user-specified number. The time.sleep(1) function pauses the program for one second in each iteration, simulating a countdown timer.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge9()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c10":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my tenth codechallenge\n")
                
                print("This code challenge contains Nested Loop (Inverted Pyramid of Stars)")
                print("\nIt uses a nested for loop structure involving loops for spaces and loops for stars to draw an inverted pyramid pattern.")
                print("\n---------------------------------------------\n")
                print("OUTPUT: ")
                codechallenge10()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "C":
            os.system("cls")
            print("---------------------------------------------")
            print(f"You've selected letter {act}")
            print("\n\tWelcome to Code Challenges 11 to 15\n")
            print("\nChoose between the given options: \n")
            print("\tc11 - CodeChallenge11\n\tc12 - CodeChallenge12\n\tc13 - CodeChallenge13\n\tc14 - CodeChallenge14\n\tc15 - CodeChallenge15\n\tc16 - CodeChallenge16\n\tm - Menu\n")
            print("---------------------------------------------")
            act1 = input("Choose the following options:  ").lower()
            if act1 == "c11":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my eleventh code challenge\n")

                print("This code challenge contains Nested Loop (Full Diamond/Hourglass Pattern)")
                print("\nIt uses two main sets of nested for loops to first draw an upright pyramid and then an inverted pyramid immediately below it, resulting in a full Diamond/Hourglass pattern.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n# print("\t\t *", end=" ")\nfor s in range(1, 12, 1):\n\tfor o in range(11, s, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(1, s, 1):\n\t\tprint("*", end=" ")\n\tfor i in range(0, s, 1):\n\t\tprint("*", end=" ")\n\tprint()\nfor s in range(1, 12, 1):\n\tfor o in range(0, s, 1):\n\t\tprint(" ", end=" ")\n\tfor f in range(10, s, -1):\n\t\tprint("*", end=" ")\n\tfor i in range(11, s, -1):\n\t\tprint("*", end=" ")\n\tprint()\n# print("\t\t *", end="")\n')
                print("OUTPUT: ")
                codechallenge11()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c12":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my twelfth code challenge\n")

                print("This code challenge contains Nested Loop (Pyramid of Numbers)")
                print("\nIt uses complex nested for loops (loops for spaces, descending numbers, and ascending numbers) to draw a classic numerical pyramid pattern, centered and symmetrical.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nfor i in range(1, 7, 1):\n\tfor x in range(7, i, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(i, 0, -1):\n\t\tprint(f, end=" ")\n\tfor e in range(2, i + 1, 1):\n\t\tprint(e, end=" ")\n\tprint()\n')
                print("OUTPUT: ")
                codechallenge12()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c13":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my thirteenth code challenge\n")

                print("This code challenge contains Nested Loop (Christmas Tree)")
                print("\nIt is a very complex pattern that combines several sets of nested loops: a small diamond for the top star, followed by three large triangles (pyramids) to form the branches, and a square base for the trunk, creating a Christmas Tree pattern.")
                print("\n---------------------------------------------\n")
                print('INPUT: \n# Diamond\nfor s in range(1, 4, 1):\n\tfor x in range(1,4,1):\n\t\tprint(" ", end=" ")\n\tfor o in range(3, s, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(1, s, 1):\n\t\tprint("*", end=" ")\n\tfor i in range(0, s, 1):\n\t\tprint("*", end=" ")\n\tprint()\nfor s in range(1, 3, 1):\n\tfor x in range(1,4,1):\n\t\tprint(" ", end=" ")\n\tfor o in range(0, s, 1):\n\t\tprint(" ", end=" ")\n\tfor f in range(2, s, -1):\n\t\tprint("*", end=" ")\n\tfor i in range(3, s, -1):\n\t\tprint("*", end=" ")\n\tprint()\n#Triangles\nfor s in range(1, 7, 1):\n\tfor o in range(6, s, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(1, s, 1):\n\t\tprint("*", end=" ")\n\tfor i in range(0, s, 1):\n\t\tprint("*", end=" ")\n\tprint()\nfor s in range(1, 7, 1):\n\tfor o in range(6, s, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(1, s, 1):\n\t\tprint("*", end=" ")\n\tfor i in range(0, s, 1):\n\t\tprint("*", end=" ")\n\tprint()\nfor s in range(1, 7, 1):\n\t\tfor o in range(6, s, -1):\n\t\tprint(" ", end=" ")\n\tfor f in range(1, s, 1):\n\t\tprint("*", end=" ")\n\tfor i in range(0, s, 1):\n\t\tprint("*", end=" ")\n\tprint()\n#Trunk\nfor s in range(5):\n\tfor o in range(4):\n\t\tprint(" ", end= " ")\n\tprint("*", end= " ")\n\tprint("*", end= " ")\n\tprint("*", end= " ")\n\tprint()\n')
                print("OUTPUT: ")
                codechallenge13()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c14":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fourteenth code challenge\n")

                print("This code challenge contains While Loop (Conditional Accumulator)")
                print("\nIt uses a while loop that runs indefinitely until a specific sentinel value (0) is entered (break). It checks if inputs are odd or even and uses a string variable (odd) to store a list of all odd numbers entered, while simultaneously calculating their sum.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nname = input("Hi! What is your name? --> ")\nprint("++++++++++++++++++++++++++++")\nprint("ODD number compiler, type "0" to terminate the loop")\nsum = 0\nodd = ""\nnumber = True\nwhile number == True:\n\tnum = eval(input("Enter a number --> "))\n\tif num % 2 == 1:\n\t\tprint("ODD number detected")\n\t\todd += str(num) + ","\n\t\tsum += num\n\t\tcontinue\n\telif num == 0:\n\t\tprint("Loop Terminated")\n\t\tbreak\n\telse:\n\t\tif num % 2 == 0:\n\t\t\tprint("EVEN number detected")\n\t\telse:\n\t\t\tprint("Invalid number")\n\t\t\tcontinue\nprint(f"Hi {"name"} the sum of all ODD number is {"sum"}")\nprint(f"All the ODD numbers you input is {"odd"}")\n')
                print("OUTPUT: ")
                codechallenge14()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c15":
                print("---------------------------------------------")
                print(f"You've selected number {act1}")
                print("\n\tWelcome to my fifteenth code challenge\n")

                print("This code challenge contains List Iteration & Validation (Watch List)")
                print("\nIt uses a while loop to let the user continuously enter anime titles. It uses a list comprehension to check the user's input against a list of pre-defined anime (case-insensitive) and adds valid titles to a watch_list.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nanim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia", "One Piece", "Chainsaw Man", "Demon Slayer", "Kurokos Basketball"]\nanime = True\nanime_lower = [anim.lower() for anim in anim]\nwatch_list = []\nwhile anime == True:\n\ttitle = input("Enter the title of the anime (or type "stop") to finish: ").lower()\n\tif title in anime_lower:\n\t\tindex = anime_lower.index(title)\n\t\torig_title = anim[index]\n\t\twatch_list.append(orig_title)\n\t\tprint(f"{"orig_title"} has been added to your anime watch list")\n\t\tcontinue\n\telif title == "stop":\n\t\tprint("You have stopped the anime recommendation lists")\n\t\tbreak\n\telse:\n\t\tprint("No such anime is found in the given anime recommendations")\n\t\tcontinue\nif watch_list:\n\tprint("\tYour selected anime list includes:")\n\tfor anim_title in watch_list:\n\t\tprint(f"- {anim_title.lower()}")\nelse:\n\tprint("\n\tYou didnt select any anime that is recommended for your watch list.")\n')
                print("OUTPUT: ")
                codechallenge15()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "c16":
                print("---------------------------------------------")
                print(f"You've selected number {act1} ")
                print("\n\tWelcome to my sixteenth code challenge\n")

                print("This code challenge contains Dictionary & File Handling (Student Information System)")
                print("\nIt is a robust menu-driven program that uses a dictionary (students_records) to store student information (using lists as values). It demonstrates advanced dictionary operations (Add, Print, Search, Delete, Edit) and uses the json module to Export and Import data to/from a file, simulating a simple database system.")
                print("\n---------------------------------------------\n")
                print('INPUT: \nimport os\nimport json\nos.system("cls")\nprint("STUDENT INFORMATION SYSTEM")\nprint("=======================================")\nstudents_records = {""}\nisTrue = True\nwhile isTrue == True:\n\tprint("Select from the options below \nA - Add Student Record\nB - Print all Record\nC - Search Student Record\nD - Delete a Student Record\nE - Edit Student Record\nF - Export Data\nG - Import Data\nH - Exit ")\n\tchoice = input("Enter your choice ---> ").lower()\n\tif choice == "a":\n\t\tos.system("cls")\n\t\tprint("Adding Student Information")\n\t\tprint(" ------------------------------------ ")\n\t\tstudent_id = input("Enter key for this student ---> ")\n\t\tfirst_name = input("Enter student first name --->").upper()\n\t\tlast_name = input("Enter student last name ---> ").upper()\n\t\tcourse = input("Enter student course ---> ").upper()\n\t\temail = input("Enter student email address ---> ")\n\t\tstudents_records[student_id] = [first_name, last_name, course, email]\n\t\tprint("Student data is saved")\n\t\tcontinue\n\telif choice == "b":\n\t\tos.system("cls")\n\t\tprint("Printing Student Record")\n\t\tfor id, record in students_records.items():\n\t\t\tprint(f"Student ID {"id"} in Student Record {"record"}")\n\t\tcontinue\n\telif choice == "c":\n\t\tos.system("cls")\n\t\tprint("Search for Student Record")\n\t\tprint("================================")\n\t\tsearch_id = input("Input Student ID to Search ---> ").lower()\n\t\tif search_id in students_records.keys():\n\t\t\tprint("Record is found")\n\t\t\t#print the record search student\n\t\t\tfor i in students_records[search_id]:\n\t\t\t\tprint(f" --- {"i"}")\n\t\telse:\n\t\t\tprint("No record found")\n\t\t\tbreak\t\n\t\tcontinue\n\telif choice == "d":\n\t\tos.system("cls")\n\t\tprint("Delete a Student Record")\n\t\tprint("================================")\n\t\tsearch_id = input("Input Student ID to Search ---> ").lower()\n\t\tif search_id in students_records.keys():\n\t\t\tprint("Record is found")\n\t\t\t#print the record search student\n\t\t\tfor i in students_records[search_id]:\n\t\t\t\tprint(f" -- {"i"}")\n\t\t\tstudents_records.pop(search_id)\n\t\t\tprint("Record is deleted")\n\t\telse:\n\t\t\tprint("No record found")\n\t\t\tbreak\n\t\tcontinue\n\telif choice == "e":\n\t\tos.system("cls")\n\t\tprint("Edit / modify a Student Record")\n\t\tsearch_id = input("Input Student ID to Search ---> ").lower()\n\t\tfor id in students_records.keys():\n\t\t\tif search_id in students_records.keys():\n\t\t\t\tprint("Record is found")\n\t\t\t#print the record search student\n\t\t\t\tfor i in students_records[search_id]:\n\t\t\t\t\tprint(f" -- {"i"}")\n\t\t\t\tfirst_name = input("Enter new student first name --->").upper()\n\t\t\t\tlast_name = input("Enter new student last name ---> ").upper()\n\t\t\t\tcourse = input("Enter new student course ---> ").upper()\n\t\t\t\temail = input("Enter new student email address ---> ")\n\t\t\t\tstudents_records[search_id][0] = first_name\n\t\t\t\tstudents_records[search_id][1] = last_name\n\t\t\t\tstudents_records[search_id][2] = course\n\t\t\t\tstudents_records[search_id][3] = email\n\t\t\t\tprint("Data Updated")\n\t\t\telse:\n\t\t\t\tprint("No record found")\n\t\t\t\tbreak\n\t\tcontinue\n\telif choice == "f":\n\t\tos.system("cls")\n\t\tprint("Export Data")\n\t\t# file name, read / write\n\t\twith open("student_records.json", "w") as new_file:\n\t\t\tjson.dump(students_records, new_file, indent=4)\n\t\tprint("Data Exported to JSON")\n\t\tcontinue\n\telif choice == "g":\n\t\tos.system("cls")\n\t\tprint("Import Data")\n\t\t# file name, read / write\n\t\twith open("student_records.json", "r") as new_file:\n\t\t\tstudent_json = json.load(new_file)\n\t\tstudents_records = student_json\n\t\tprint("Data Imported to JSON")\n\t\tcontinue\n\telif choice == "h":\n\t\tprint("Exiting the program.....")\n\t\tbreak\n\telse:\n\t\tprint("Invalid Input")\n\t\tcontinue\n')
                print("OUTPUT: ")
                codechallenge16()
                print("\n---------------------------------------------\n")
                continue
            elif act1 == "m":
                print("Proceeding to Menu...")
                continue
            else:
                print("Invalid input, try again")
                continue

        elif act == "S": 
            print("Stopping The Program... ")
            break
        elif act == "M":
            os.system("cls")
            print("Going Back to Menu")
            continue
        else:
            os.system("cls")
            print("Invalid input, choose only between the given choices.")
            continue
    
    else:
        os.system("cls")
        print("Error, Choose only in the given options..")
        continue
