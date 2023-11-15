#Name: SALMA YASSER SADIK  Matric NO.: A19MJ3069
#  QUESTION 2
# You are tasked with implementing a simple program to analyze a given string. Write a Python 
# program that performs the following tasks:
def analyze_string(input_str): #Takes a string as input from the user.
    """Analyze the given string"""
    total_characters = len(input_str) # this line is changed if the total_characters = 0, it can't analyze the string from user. 
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    is_palindrome = False # intialize as False 

    # Analyze the string
    for char in input_str:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    # Check if the string is a palindrome
    reversed_string = input_str[::-1]
    if input_str == reversed_string:
        is_palindrome = True

    # Print the results # i have removed the def main function
    print("Total characters:", total_characters)  # The total number of characters in the string
    print("Uppercase letters:", uppercase_count) #The number of uppercase letters in the string
    print("Lowercase letters:", lowercase_count) #The number of lowercase letters in the string
    print("Digits:", digit_count) # The number of digits in the string
    print("Is the string a palindrome:", is_palindrome) #Whether the string is a palindrome or not

# Get the string from the user
print(f"\nExample Input:")  # print the statement Example input
input_str = input("Enter a string: ")

# Analyze and print the results
analyze_string(input_str)