from activity25_1 import *
name = input("Hi, What is your name? --> ")

print(f'Welcome {name}, to my compuler program ')

isContinue = True

while isContinue == True:
    print("Select a program")
    print('A - Activity1\nB - Activity2\nC - Activity3\nD - Activity4\nE - Exit')

    choose = input("What program / code would you like to run --> ").lower()

    if choose == 'a':
        activity1()
        continue
    elif choose == 'b':
        activity2()
        continue
    elif choose == 'c':
        activity3()
        continue
    elif choose == 'd':
        activity4()
        continue
    elif choose == 'e':
        print("Exiting the system")
        break
    else:
        print("Error, please only select the given choices")