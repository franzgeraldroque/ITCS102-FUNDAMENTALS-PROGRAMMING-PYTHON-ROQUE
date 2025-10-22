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
