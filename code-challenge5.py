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
