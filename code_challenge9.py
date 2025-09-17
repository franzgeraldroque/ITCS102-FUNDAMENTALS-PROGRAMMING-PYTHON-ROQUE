import time
print("COUNTDOWN TIMER SIMULATOR")
num = int(input("Enter a number --> "))
print("Countdown started: ")
for i in range(num, 0, -1):
    print(i)
    time.sleep(1)
print("TAKBO KAIBIGAN!!")
