#Program to check if a person can vote using his age | Menu-Driven

while True:
    # Get user input for age
    age = int(input("Enter your age: "))
    
    # Check if the person is allowed to vote based on age
    if age >= 18:
        print("Person is allowed to vote")
    else:
        print("Person is not allowed to vote")

    # Ask the user if they want to continue
    input_str = input("To continue, press 'Y'. To exit, press another key: ")

    # Convert the input to uppercase for case-insensitivity
    input_char = input_str.upper()

    # Check if the user wants to continue
    if input_char != 'Y':
        break  # Exit the loop if the input is not 'Y'

# Print a message when the program is terminated
print("Program Terminated")
