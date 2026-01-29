word = input("Enter a word --> ")
length = len(word)

num = []
for i in range(length):
    num1 = int(input("Enter a number -->"))
    num.append(num1)

def average(list):
    total_avg = 0
    for x in list:
        total_avg = total_avg + num
        

# def average(list):
#     total = 0
#     for num in list:
#         total = total + num1
    
#     average = total / len(list)
#     return average

# def compare(average, length):
#     if length > average:
#         print('The length of the word is greater')
#     elif average > length:
#         print('The average is greater')
#     else:
#         print('Both are equal')

# word = input("Enter a word --> ")

# length = len(word)

# num = []

# for i in range(length):
#     num1 = float(input("Enter a number --> "))
#     num.append(num1)

# total_num = average(num1)

# print(f'The length of the word is {length}')
# print(f'The average of numbers is {num}')
# print(f'The length of the word {word} is {average} ')
