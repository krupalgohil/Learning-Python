class BankSystem:
    def __init__(self):
        # accounts stored as {account_number: {"name": str, "balance": float}}
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter new account number: ")
        if account_number in self.accounts:
            print("Account already exists!")
            return
        name = input("Enter account holder's name: ")
        self.accounts[account_number] = {"name": name, "balance": 0.0}
        print(f"Account created successfully for {name} with account number {account_number}.")

    def deposit(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found!")
            return
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Invalid amount!")
            return

        self.accounts[account_number]["balance"] += amount
        print(f"Deposited ${amount:.2f} successfully.")

    def withdraw(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found!")
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive!")
                return
        except ValueError:
            print("Invalid amount!")
            return

        if amount > self.accounts[account_number]["balance"]:
            print("Insufficient balance!")
            return
        self.accounts[account_number]["balance"] -= amount
        print(f"Withdrew ${amount:.2f} successfully.")

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found!")
            return
        balance = self.accounts[account_number]["balance"]
        print(f"Account balance for {account_number} is: ${balance:.2f}")

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return
        print("All bank accounts:")
        for acc_num, info in self.accounts.items():
            print(f"Account Number: {acc_num}, Name: {info['name']}, Balance: ${info['balance']:.2f}")

    def run(self):
        while True:
            print("\nWelcome to the Bank System")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Show All Accounts")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.show_all_accounts()
            elif choice == "6":
                print("Thank you for using the Bank System. Goodbye!")
                break
            else:
                print("Invalid choice. Please select between 1-6.")


if __name__ == "__main__":
    bank = BankSystem()
    bank.run()
