class BankAccount:
    
    def __init__(self, account_holder, balance=0.0):
        # Initialize account holder's name and balance in the constructor
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount  # Add amount to balance
            print(f"Deposited: {amount:.2f}  Successfully.")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount  # Subtract amount from balance
                print(f"Withdrew: {amount:.2f} Successfully.")
            else:
                print("Error: Insufficient funds.") # Check if enough balance is available
        else:
            print("Error: Withdrawal amount must be positive.") # Show error if amount is negative

    def display_balance(self):
        # Method to display the current balance
        print(f"Current Balance for {self.account_holder}: {self.balance:.2f}") # Display balance with two decimal places


if __name__ == "__main__":
    # Create two bank account instances
    acc1 = BankAccount("Alice") 
    acc2 = BankAccount("Bob")

    while True:
        # Display bank menu options
        print("\n--------- Bank Menu ---------") 
        print("1. Deposit")  
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ") # Get user choice

        if choice == '1': 
            amount = float(input("Enter amount to deposit: ")) # Get deposit amount from user
            acc1.deposit(amount)  # Call deposit method
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            acc1.withdraw(amount)  # Call withdraw method
        elif choice == '3':
            acc1.display_balance()  # Call display_balance method
        elif choice == '4':
            print("Thank you for using bank")  # Exit message
            break
        else:
            print("Invalid option. Please try again.")  # Handle invalid input