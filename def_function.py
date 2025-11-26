#Activities
def activity1():
    print("Hello Hanniel my BFF") 

def activity2():
    name = input("What is your name .?")
    print("Hello", name, "Welcome to the Matrix") 

def activity3():
    print("Happy\n\tMonday,")
    print("BSIT 1A\n\t from DLL")
    print("Hi ex, \n\t kakalimutan na kita")
    print("The quick snatcher runs\n\t over\n\t manila city") 

def activity4():
    name = input("Enter a string -> ")
    print("Your name has ", len(name), "character") 
def activity5():
    something = eval(input("Input something --> "))
    print("The data type of something is",type(something))
    answer = 5 + something
    print("The answer is ", answer) 

def activity6():  
    n1 = eval(input("Enter the first number : "))
    n2 = eval(input("Enter the second number : "))
    s = n1 + n2
    d = n1 - n2
    p = n1 * n2
    q = n1 / n2
    print ("\nThe sum of",n1, "and" ,n2, "is",s)
    print ("The difference of",n1, "and" ,n2, "is" ,d)
    print("The product of",n1, "and" ,n2, "is" , p)
    print ("The quotient of",n1, "and",n2, "is", q)
    print(n1, "exponent by",n2, "is", n1**n2)
    print ("The remainder of",n1, "and" , n2, "is", n1 % n2)
    print("The floor division of",n1, "and" ,n2, "is" ,n1//n2) 

def activity7():   
    f = 7
    print("the value of a is ", f)
    f += 17
    f = 3
    f *= 2
    f = 6
    print("the value of a is ", f)

def activity8():
    ex = 18
    ako = 18
    print(ex > ako)
    birthday1 = 3
    birthday2 = 17
    print(birthday1 != birthday2)

def activity9():
    #valorant = 'stress'
    valorant = 'joy'
    sleep = 'rest'
    #print(valorant == 'stress')
    #print(sleep == 'rest')
    #print((valorant == 'stress') and (sleep == 'rest'))
    print((valorant == 'stress') or (sleep == 'rest'))
    print(not((valorant == 'stress') or (sleep == 'rest')))

def activity10():
    #tricycle fare
    name = input("Input your name ---> ")
    isStudent = input("Are you a student (Yes / No) --> ")
    fare = eval(input("bayad --> "))
    if isStudent.lower() == "yes":
        discount = fare * .20
        new_fare = fare - discount
        print("Hi", name, " student discount is ", discount, " Discounted fare is ", new_fare)
    else:
        print("Sorry", name, " you are not eligible for student discount")

def activity11():
    #1 to 20 cold
    #21 to 30 luke warm
    #31 to 40 warm
    #41 to 50 hot
    #51 and above boiling point
    temp = eval(input("Enter temperature --> "))
    if temp >= 1 and temp <= 20:
        print("Temperature outside is cold")
    elif temp >= 21 and temp <= 30:
        print("Temperature outside is luke warm")
    elif temp >= 31 and temp <= 40:
        print("Temperature outside is warm")
    elif temp >= 41 and temp <= 50:
        print("Temperature outside is hot")
    elif temp >= 51:
        print("Temperature outside is super duper hot")
    else:
        print("Invalid temperature")

def activity12():

    #print("Hello World")
    #name = input("Enter your name: ")
    #print("Hello", name, "say Hi to your future girlfriend")
    #print hello world 10 times
    for truepa in range(1, 100, 2):
        print(truepa, "- kamusta sa aking magiting na kaibigan")

def activity13():
    #using for loop, ask user to input 10 numbers
    #after input, get the summation of all the numbers
    num = 0
    for cashg in range(1, 11):
        number = eval(input('Enter a number --> '))
        num += number
        print('ang laman ng imong gcash ay',num)
    print("ang imong gcash ay may laman na",num, "pidi ba akong makikurot kahit pang lud lang")

def activity14():
    #ascending numbers
    for aports in range(20, 0, -1):
        print(aports)

def activity15():
    #print("ODD NUMBER SUMMATION")
    #print("INPUT 10 ODD NUMBERS")
    odd_sum = 0
    for i in range(1,11,1):
        num = eval(input("Enter a number -->"))
        if num % 2 == 1:
            odd_sum += num
    print(f"The sum of all odd number is: {odd_sum}")

def activity16():
    #print("Print numbers 1 to 10 horizontally")
    for i in range(1,11,1):
        print(i,end=", ")

def activity17():
    for i in range(1,11,1):
        for x in range(1,11,1):
            print( x, end=" ")
        print()

def activity18():
    for i in range(1, 11, 1):
        for x in range(1, i, 1):
            print(x, end=" ")
        print()

def activity19():
    for i in range(1, 11, 1):
        for x in range(1, i, 1):
            print("*", end=" ")
        print()

def activity20():
    for i in range(1, 11, 1):
        for x in range(1, i, 1):
            print(" ", end=" ")
        for f in range(10, i, -1):
            print("*", end=" ")
        print()

def activity21():
    isDirty = True

    while isDirty == True:
        confirm = input("Gusto mo bang magpatuloy pa sa paglalaba? (tara / ayaw ko)-->").lower()

        if confirm == "tara":
            print("Tayo'y magpapatuloy")
            continue
        elif confirm == "ayaw ko":
            print("Itigil na natin to!!")
            break
        else:
            print("Wala ka naman sa tama eh")
            continue

def activity22():
    import random
    num = random.randint(1,10)
    tries = 0
    istrue = True
    while istrue == True:
        guesser = eval(input("Guess a number between 1-10: "))
        tries += 1
        if guesser == num:
            print("Congratulations")
            print(f"The number is {num}")
            print(f"You only took {tries} tries")
            break
        else:
            print("The number you picked is invalid, please continue...")
        continue

def activity23():
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

def activity24():
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

def activity25():
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
            
def activity26():
    #Create a dictionary
    Language = {"Filipino": "kumain ka na?", "Englisn": "did you ate?", "Spanish": "has comido?", "French": "as-tu mangé", "Japanese": "食べましたか"}
    print("Nagkaon ka na?")
    print("\nKumain ka na? in every language")
    for i,x in Language.items():
        print(f"\tLanguage for kumain ka na? --> {i}")
    kaon = input("Pick only one language: \n").capitalize()
    print({Language[kaon]})

def activity27():
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

def activity28():
    #Step 1 
    import pygame
    import time
    import random

    # Initialize Pygame
    pygame.init()

    # Screen size
    width = 600
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Colors (RGB)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    # Game speed and block size
    clock = pygame.time.Clock()
    speed = 10
    snake_block = 10

    # Font for messages
    font_style = pygame.font.SysFont(None, 30)


    #Step 2 
    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    #Step 3 
    def game_loop():
        game_over = False
        game_close = False

        # Starting position of the snake
        x = width / 2
        y = height / 2

        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        # Generate first food
        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10

        while not game_over:

            # Loss screen
            while game_close:
                screen.fill(black)
                message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
                screen.blit(message, [width / 6, height / 3])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            # Event handling (keyboard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            # Check if snake hits the wall
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            # Update position
            x += x_change
            y += y_change

            # Draw background and food
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # Add snake head
            snake_head = [x, y]
            snake_list.append(snake_head)

            # Remove extra segments if not growing
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            # Draw the snake
            draw_snake(snake_list)

            # Update display
            pygame.display.update()

            # Check if snake eats food
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1

            # Control game speed
            clock.tick(speed)

        # Quit Pygame
        pygame.quit()
        quit()

    # Start the game
    game_loop()



#Code Challenges
def codechallenge1():
    name = input("What is your name?")
    print("\t\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t♦\t\t\tHI\t\t\t♦ \n\n\n \t♦\t\t\t" , name , "\t\t\t♦ \n\n\n \t\t♦\t\t\t\t\t\t♦ \n\n\n \t\t\t♦\t\t\t\t♦ \n\n\n \t\t\t\t♦\t\t♦ \n\n\n \t\t\t\t\t♦") 

def codechallenge2():
    amount = eval(input("Enter amount to deposit :"))
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    print("\nHere is a breakdown in PH denomination: ")
    for denom in denominations:
        count = amount // denom
        amount = amount % denom
        print(count, "-", denom)
    print("\nSana lahat ng tao ganito... ")

def codechallenge3():
    from getpass import getpass
    username = 'Franzgeraldroque2'
    pwd = 'franzroque17'
    uname = input('input username -->' )
    p_input = getpass('enter password --> ')
    #valid username or password
    if username == uname and pwd == p_input :
        print("Access granted")
    else:
        print("Access denied")

def codechallenge4():
    #even = 2,4,6,8,10
    #odd = 1,3,5,7,9
    number = int(input('Input a number --> '))
    if number % 2 == 0 :
        print(" number = even")
    else:
        print(" number = odd")

def codechallenge5():
    print("Welcome to the Anime Recommender ⛩️🌸🍥☯🍜")
    print("Answer a few questions to find your next anime")
    genre = input("What genre do you like? (action, romance, horror)--> ").lower()
    time = input("How long should the anime be? (short, medium, long)--> ").lower()
    decade = input("Which decade? (2000s, 2010s, 2020s)--> ")
    if genre == 'action':
        print("You selected:",genre)
        if time == 'long' and decade == '2000s':
                print("Here are the list of Long Anime Action in 2000s")
                print("Anime recommended for action are the following: \n 1.Naruto \n 2.Bleach \n 3.Death Note")
        else:
            print("Sorry, no action anime found for that time and decade.")
    elif genre == 'romance':
        print("You selected:",genre)
        if time == 'medium' and decade == '2010s':
                print("Here are the list of Medium Anime Romance in 2010s")
                print("Anime recommended for romance are the following: \n 1.Your Name \n 2.Your Lie in April \n 3.Weathering with You")
        else:
            print("Sorry, no romance anime found for that time and decade.")
    elif genre == 'horror':
        print("You selected:",genre)
        if time == 'short' and decade == '2020s':
                print("Here are the list of Short Anime Horror in 2020s")
                print("Anime recommended for romance are the following: \n 1.The Grimm Variations \n 2.Mieruko-chan \n 3.Junji Ito Maniac: Japanese Tales of the Macabre")
        else:
            print("Sorry, no horror anime found for that time and decade.")
    else:
        print("Sorry", genre, "is not on the genre choices")

def codechallenge6():
    number = eval(input("Enter a number --> "))
    factorial = 1
    for i in range(number, 0, -1):
        factorial1 = factorial
        factorial *= i
        print(i, "*", factorial1, "=", factorial)
    print("The factorial is", factorial)

def codechallenge7():
    print("ODD NUMBER SUMMATION")
    print("Maglagay ng sampung numero")
    odd = 0
    for i in range(10):
        number = eval(input("ilagay mo ang numero beybe -->"))
        if number %2 != 0:
            odd += number
        else:
            print("ang numero", number, "ay hindi odd number")
    print("ang kabuuan ng pangkalahatang odd number ay", odd)

def codechallenge8():
    num = eval(input("Enter a number --> "))
    print(f"The multiplication table of {num} is: ")
    for i in range(1,11):
        multiply = num * i
        print(f" {num} * {i} = {multiply}") 

def codechallenge9():
    import time
    print("COUNTDOWN TIMER SIMULATOR")
    num = int(input("Enter a number --> "))
    print("Countdown started: ")
    for i in range(num, 0, -1):
        print(i)
        time.sleep(1)
    print("TAKBO KAIBIGAN!!")

def codechallenge10():
    print("\t\t *", end="" )
    for i in range(1, 11, 1):
        for x in range(10, i, -1):
            print(" ", end=" ")
        for f in range(1, i, 1):
            print("*", end=" ")
        for e in range(1, i, 1):
            print("*", end=" ")
        print()

def codechallenge11():
    # print("\t\t *", end=" ")
    for s in range(1, 12, 1):
        for o in range(11, s, -1):
            print(" ", end=" ")
        for f in range(1, s, 1):
            print("*", end=" ")
        for i in range(0, s, 1):
            print("*", end=" ")
        print()
    for s in range(1, 12, 1):
        for o in range(0, s, 1):
            print(" ", end=" ")
        for f in range(10, s, -1):
            print("*", end=" ")
        for i in range(11, s, -1):
            print("*", end=" ")
        print()
    # print("\t\t *", end="")

def codechallenge12():
    for i in range(1, 7, 1):
        for x in range(7, i, -1):
            print(" ", end=" ")
        for f in range(i, 0, -1):
            print(f, end=" ")
        for e in range(2, i + 1, 1):
            print(e, end=" ")
        print()

def codechallenge13():
    # Diamond
    for s in range(1, 4, 1):
        for x in range(1,4,1):
            print(" ", end=" ")
        for o in range(3, s, -1):
            print(" ", end=" ")
        for f in range(1, s, 1):
            print("*", end=" ")
        for i in range(0, s, 1):
            print("*", end=" ")
        print()
    for s in range(1, 3, 1):
        for x in range(1,4,1):
            print(" ", end=" ")
        for o in range(0, s, 1):
            print(" ", end=" ")
        for f in range(2, s, -1):
            print("*", end=" ")
        for i in range(3, s, -1):
            print("*", end=" ")
        print()
    #Triangles
    for s in range(1, 7, 1):
        for o in range(6, s, -1):
            print(" ", end=" ")
        for f in range(1, s, 1):
            print("*", end=" ")
        for i in range(0, s, 1):
            print("*", end=" ")
        print()
    for s in range(1, 7, 1):
        for o in range(6, s, -1):
            print(" ", end=" ")
        for f in range(1, s, 1):
            print("*", end=" ")
        for i in range(0, s, 1):
            print("*", end=" ")
        print()
    for s in range(1, 7, 1):
        for o in range(6, s, -1):
            print(" ", end=" ")
        for f in range(1, s, 1):
            print("*", end=" ")
        for i in range(0, s, 1):
            print("*", end=" ")
        print()
    #Trunk
    for s in range(5):
        for o in range(4):
            print(" ", end= " ")
        print("*", end= " ")
        print("*", end= " ")
        print("*", end= " ")
        print()

def codechallenge14():
    name = input("Hi! What is your name? --> ")
    print("++++++++++++++++++++++++++++")
    print("ODD number compiler, type '0' to terminate the loop")
    sum = 0
    odd = ""
    number = True
    while number == True:
        num = eval(input("Enter a number --> "))
        if num % 2 == 1:
            print("ODD number detected")
            odd += str(num) + ","
            sum += num
            continue
        elif num == 0:
            print("Loop Terminated")
            break
        else:
            if num % 2 == 0:
                print("EVEN number detected")
            else:
                print("Invalid number")
                continue
    print(f"Hi {name} the sum of all ODD number is {sum}")
    print(f"All the ODD numbers you input is {odd}")

def codechallenge15():
    anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia", "One Piece", "Chainsaw Man", "Demon Slayer", "Kuroko's Basketball"]
    anime = True
    anime_lower = [anim.lower() for anim in anim]

    watch_list = []

    while anime == True:
        title = input("Enter the title of the anime (or type 'stop') to finish: ").lower()

        if title in anime_lower:
            index = anime_lower.index(title)
            orig_title = anim[index]
            watch_list.append(orig_title)
            print(f'{orig_title} has been added to your anime watch list')
            continue

        elif title == 'stop':
            print('You have stopped the anime recommendation lists')
            break

        else:
            print("No such anime is found in the given anime recommendations")
            continue

    if watch_list:
        print("\tYour selected anime list includes:")
        for anim_title in watch_list:
            print(f"- {anim_title.lower()}")
    else:
        print("\n\tYou didn't select any anime that is recommended for your watch list.")

def codechallenge16():
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
            print("Delete a Student Record")
            print("================================")

            search_id = input("Input Student ID to Search ---> ").lower()
            
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
            os.system('cls')
            print("Edit / modify a Student Record")

            search_id = input("Input Student ID to Search ---> ").lower()
            
            if search_id in students_records.keys():
                print("Record is found")
                        #print the record search student
                for i in students_records[search_id]:
                    print(f' -- {i}')
                        
                first_name = input("Enter new student first name --->").upper()
                last_name = input("Enter new student last name ---> ").upper()
                course = input("Enter new student course ---> ").upper()
                email = input("Enter new student email address ---> ")

                students_records[search_id][0] = first_name
                students_records[search_id][1] = last_name
                students_records[search_id][2] = course
                students_records[search_id][3] = email

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
            
            print("Data Exported to JSON")
            continue
        elif choice == 'g':
            os.system("cls")
            print("Import Data")
                    # file name, read / write
            with open("student_records.json", 'r') as new_file:
                student_json = json.load(new_file)

            students_records = student_json
            print("Data Imported to JSON")
            continue

        elif choice == 'h':
            print("Exiting the program.....")
            break
        else:
            print("Invalid Input")
            continue
