print("Adding Data to directory")
print("=========================================")
go_lang = True

empty_directory = {}

#if printing values .values()
#if printing both the values and items .items()

def anim_print():
    for i,j in empty_directory.items():
        print(f'Key - {i}, Title - {j}')

def for_search():
    print("Searching ...")
    print(f"Results shows {empty_directory[key].upper()} on our database")

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
        for_search()
    elif choice == 'n':
        print("Stopping the program ...")
        break
    else:
        print("Error, pick between the choices only")