# # title = input("Enter the title of the anime (or type 'stop' to finish: )")

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
# anime = True

# # Convert all anime titles to lowercase for comparison
# anim_lower = [a.lower() for a in anim]

# while anime:
#     title = input("Enter the title of the anime (or type 'stop' to finish): ").strip().lower()

#     if title == 'stop':
#         print('You have stopped the anime recommendation list.')
#         break

#     elif title in anim_lower:
#         # Find the original title with correct casing
#         original_title = anim[anim_lower.index(title)]
#         print(f"'{original_title}' has been added to your anime watch list.")
#         continue

#     else:
#         print("No such anime is found in the given anime recommendations.")
#         continue


# anim = ["Jujutsu Kaisen", "Naruto", "Attack on Titan", "MyHeroAcademia"]
# for anime in anime:
#     print(anime)