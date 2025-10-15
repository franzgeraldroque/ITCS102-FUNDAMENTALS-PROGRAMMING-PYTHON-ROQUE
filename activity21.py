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