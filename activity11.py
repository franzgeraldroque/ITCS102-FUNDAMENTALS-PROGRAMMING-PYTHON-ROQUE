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