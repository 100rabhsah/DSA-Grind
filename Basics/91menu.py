#Program to check if a student passes/fails using his grade | Menu Driven

while True:
    marks = int(input("Enter your marks: "))
    
    if marks >100 or marks<0:
        print("invaild marks")
    elif marks >= 33:
        print("Pass") 
    else:
        print("Fail")

    # Ask the user if they want to continue
    input_str = input("To continue, press 'Y'. To exit, press another key: ")

    # Convert the input to uppercase for case-insensitivity
    input_char = input_str.upper()

    # Check if the user wants to continue
    if input_char != 'Y':
        break  # Exit the loop if the input is not 'Y'

print("Program Terminated")
