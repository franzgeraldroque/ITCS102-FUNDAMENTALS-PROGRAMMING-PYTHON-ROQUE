anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia"]
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

# anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia"]
# for anime in anime:
#     print(anime)