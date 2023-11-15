#Name: SALMA YASSER SADIK  Matric NO.: A19MJ3069
# QUESTION 1
# You are tasked with creating a Python program to calculate the sum of the first n terms in an 
# arithmetic sequence. Write a program that:

def is_it_positive_integer(n):    #Check if a number is a positive integer.
    try: # convert number to integer for sum n represents the sum value
        n = int(n)
    except ValueError:   # If an error , Then the number is not an integer
        return False
    # Check positive number or not
    return n > 0  

def input_value(user):  #find input from the user, to make sure its a positive integer.
    while True:
        n = input(user)
        if is_it_positive_integer(n):
            return int(n)
        else:
            print("Enter a positive integer!")


def sum_calculation(a, d, n): #Calculates and prints the sum of the first n terms of the arithmetic sequence
    return n * (2 * a + (n - 1) * d) // 2

# Takes two positive integers, a and d, as input from the user. These represent the first term 
# and the common difference of an arithmetic sequence.
print(f"\nExample Input:")  # print the statement Example input
a = input_value("Enter the first term (a) of the arithmetic sequence:")   # print the statement and ask for any input integer for a 
d = input_value("Enter the common difference (d) of the arithmetic sequence: ") # print the statement and ask for any input integer for d
n = input_value("Enter the number of terms (n) to sum: ") # print the statement and ask for any input integer for n

# Calculates and prints the sum of the first n terms of the arithmetic sequence.
sequence_sum = sum_calculation(a, d, n)
print(f"\nExample Output:")  # print the statement Example output
print("The sum of the first {} terms of the arithmetic sequence is: {}".format(n, sequence_sum)) # print the statement with the total sum of all input values 