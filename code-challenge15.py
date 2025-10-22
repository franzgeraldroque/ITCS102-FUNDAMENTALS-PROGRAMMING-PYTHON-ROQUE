anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia"]
anime = True
anime_lower = [anim.lower for anim in anim]

while anime == True:
    title = input("Enter the title of the anime (or type 'stop') to finish:")

    if title in anim == ['Jujutsu Kaisen', 'Naruto', 'Attack on Titan', 'MyHeroAcademia']: 
        print(f'{anim} has been added to your anime watch list')
        continue

    elif title == 'stop':
        print('You have stopped the anime recommendation lists')
        break

    else:
        print("No such anime is found in the given anime recommendations")
        continue

# anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia"]
# for anime in anime:

#     print(anime)
