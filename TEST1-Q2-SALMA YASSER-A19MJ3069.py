def analyze_string(input_string):
    total_chars = len(input_string)
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    is_palindrome = False

    # Analyze the string
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    # Check if the string is a palindrome
    reversed_string = input_string[::-1]
    if input_string == reversed_string:
        is_palindrome = True

    # Print the results
    print("Total number of characters:", total_chars)
    print("Number of uppercase letters:", uppercase_count)
    print("Number of lowercase letters:", lowercase_count)
    print("Number of digits:", digit_count)
    print("Is the string a palindrome:", is_palindrome)

# Get the string from the user
input_string = input("Enter a string: ")

# Analyze and print the results
analyze_string(input_string)