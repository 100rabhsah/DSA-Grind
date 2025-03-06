#Program to calculate Electricity Bill

def calculate_bill(units):
    if units <= 50:
        bill = units * 1.25
    elif units <= 100:
        bill = (50 * 1.25) + (units - 50) * 2.25
    elif units <= 200:
        bill = (50 * 1.25) + (50 * 2.25) + (units - 100) * 4.00
    elif units <= 300:
        bill = (50 * 1.25) + (50 * 2.25) + (100 * 4.00) + (units - 200) * 5.50
    else:
        bill = (50 * 1.25) + (50 * 2.25) + (100 * 4.00) + (100 * 5.50) + (units - 300) * 7.50
    
    return round(bill, 2)

# Menu-driven program
while True:
    print("\nJharkhand Electricity Bill Calculator")
    print("1. Calculate Bill")
    print("2. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        units = int(input("Enter number of units consumed: "))
        if units < 0:
            print("Invalid input! Units cannot be negative.")
        else:
            bill_amount = calculate_bill(units)
            print(f"Electricity Bill: ₹ {bill_amount}")
    elif choice == 2:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
