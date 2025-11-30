from activity27 import *
from activity23 import *
from activity24 import *
def activity27():
    print("Welcome to Activity27")
    
    print("Adding Data to directory")
    print("=========================================")
    go_lang = True

    empty_directory = {}

    #if printing values .values()
    #if printing both the values and items .items()

    def anim_print():
        for i,j in empty_directory.items():
            print(f'Key - {i}, Title - {j}')

    def forsearch(search_key):
        print("Searching ...")
        if search_key in empty_directory:
            print(f"Result shows {empty_directory[search_key].upper()} in our database")
        else:
            print("No results found for that key.")

    while go_lang == True:
        key = input("Input keys for this anime ---> ")

        anim = input("Enter the anime title ---> ")

        empty_directory[key] = anim

        choice = input("Would you like to continue adding anime: \ny - Yes\nn - No\np - Print\ns - Search:\n ").lower()
        

        if choice == 'y':
            print("Continuing ... ")
            continue
        elif choice == 'p':
            # if empty_directory:
            #     print("\nThe anime you have entered are: ")
            #     for anim in empty_directory.values():
            #         print(f'Anime - {anim}')
            anim_print()
            continue
        elif choice == 's':
            code = input("Enter the code of the anime: ")
            forsearch(code)
        elif choice == 'n':
            print("Stopping the program ...")
            break
        else:
            print("Error, pick between the choices only")

def activity23():
    print("This is my Activity23")
    nm = ['apple','hotdog','orange','watermelon','egg']
    nm.append('mango')   #add an item to the last of the list
    print(nm)
    nm.pop()    #remove the last item
    print(nm)
    nm.insert(0,'watermelon')   #add item in dif position
    print(nm)
    for i in nm:
        print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

    mi = 'Franz Gerald L. Roque'
    for u in mi:
        print(u)    #Will print my name from f to e
    print("\nReversed\n")
    for q in mi[::-1]:  #will print my name in reverse from n to j
        print(q)

def activity23():
    print("This is my Activity24")
    
    def greeter(name):
        print(f"Hi {name}, kamusta ka na?")

    def summation(x):
        sum = 0
        for i in range (x,0,-1):
            sum += i
        print(f"The sum of {x} is {sum}")

    greeter("Sofia")
    greeter("Diaz")
    greeter("Nista")
    summation(18)
    summation(11)

