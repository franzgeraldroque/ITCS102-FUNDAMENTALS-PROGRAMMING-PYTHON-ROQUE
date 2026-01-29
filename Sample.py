# Function (a): Calculates the average of the numbers in the list
def calculate_average(my_numbers):
    total_sum = 0
    # Loop through the list to add everything up
    for n in my_numbers:
        total_sum = total_sum + n
    
    # Simple division to get the average
    average = total_sum / len(my_numbers)
    return average

# Function (b): Compares average with word length and displays result
def compare_results(avg, word_len):
    if word_len > avg:
        print("The word length is greater than the average.")
    elif avg > word_len:
        print("The average is greater than the word length.")
    else:
        print("The word length and average are equal.")

# --- START OF PROGRAM ---

# 1. Ask the user for a word
user_word = input("Enter a word: ")

# 2. Determine the length of the word
word_length = len(user_word)

# 3. Ask for numbers (must be equal to the length of the word)
number_list = []
print("The word has", word_length, "characters.")
print("Please enter", word_length, "numbers:")

# 4. Use a loop to get inputs and store them in the list
for i in range(word_length):
    num = float(input("Enter number: "))
    number_list.append(num)

# 5. Compute the average using the function
final_avg = calculate_average(number_list)

# 6. Display the results clearly
print("\n--- RESULTS ---")
print("List of numbers:", number_list)
print("Length of the word:", word_length)
print("Average of the numbers:", final_avg)

# Call the second function to show the comparison message
compare_results(final_avg, word_length)
