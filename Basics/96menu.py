#Menu-Driven Program for Bank Management System

# Bank Management System

class BankAccount:
    def __init__(self, name, address, acc_type, balance):
        self.name = name
        self.address = address
        self.acc_type = acc_type.upper()  # S for Saving, C for Current
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nAvailable Balance: {self.balance}")
        else:
            print("\nInvalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nAvailable Balance: {self.balance}")
        elif amount > self.balance:
            print("\nInsufficient balance!")
        else:
            print("\nInvalid withdrawal amount!")

    def display_account(self):
        print("\nName:", self.name)
        print("Address:", self.address)
        print("Type:", self.acc_type)
        print("Balance:", self.balance)


# Main program
account = None  # No account initially

while True:
    print("\n1) Open Account")
    print("2) Deposit Money")
    print("3) Withdraw Money")
    print("4) Display Account")
    print("5) Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':  
        if account is not None:
            print("\nAccount already exists!")
        else:
            name = input("\nEnter your full name: ")
            address = input("Enter your address: ")
            acc_type = input("What type of account you want to open saving(S) or Current(C): ").strip().upper()
            if acc_type not in ['S', 'C']:
                print("\nInvalid account type! Choose S or C.")
                continue
            balance = float(input("Enter how much money you want to deposit: "))
            account = BankAccount(name, address, acc_type, balance)
            print("\nAccount Created Successfully\n-------------------------------------------------")

    elif choice == '2':  
        if account is None:
            print("\nNo account found! Open an account first.")
        else:
            amount = float(input("\nEnter how much money you want to deposit: "))
            account.deposit(amount)
            print("-------------------------------------------------")

    elif choice == '3':  
        if account is None:
            print("\nNo account found! Open an account first.")
        else:
            amount = float(input("\nEnter how much money you want to withdraw: "))
            account.withdraw(amount)
            print("-------------------------------------------------")

    elif choice == '4':  
        if account is None:
            print("\nNo account found! Open an account first.")
        else:
            account.display_account()
            print("\n-------------------------------------------------")

    elif choice == '5':  
        print("\nThank you for using our Bank Management System!")
        break

    else:
        print("\nInvalid choice! Please select from 1-5.")
