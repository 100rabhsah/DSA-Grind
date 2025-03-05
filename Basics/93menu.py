#Program to print the name of month using the month number | Menu-Driven

def get_month_name(month_num):
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return months.get(month_num, "Invalid month number")

while True:
    print("\nMENU:")
    print("1. Enter month number")
    print("2. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        month_num = int(input("Enter month number (1-12): "))
        print("Month:", get_month_name(month_num))
    elif choice == 2:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
