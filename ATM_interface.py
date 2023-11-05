class ATM:
    def __init__(self):
        self.users = {
            "user1": {"pin": "1234", "balance": 1000},
            "user2": {"pin": "5678", "balance": 1500},
        }
        self.current_user = None
        self.transactions = []

    def authenticate_user(self):
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")
        if user_id in self.users and self.users[user_id]["pin"] == pin:
            self.current_user = user_id
            print("Authentication successful.")
        else:
            print("Authentication failed. Please try again.")

    def check_balance(self):
        balance = self.users[self.current_user]["balance"]
        print(f"Your balance is ${balance}")

    def withdraw(self, amount):
        if amount <= self.users[self.current_user]["balance"]:
            self.users[self.current_user]["balance"] -= amount
            self.transactions.append(f"{self.current_user} withdrew ${amount}")
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.users[self.current_user]["balance"] += amount
        self.transactions.append(f"{self.current_user} deposited ${amount}")
        print(f"Deposited ${amount}")

    def transfer(self, to_user, amount):
        if to_user in self.users and amount <= self.users[self.current_user]["balance"]:
            self.users[self.current_user]["balance"] -= amount
            self.users[to_user]["balance"] += amount
            self.transactions.append(f"{self.current_user} transferred ${amount} to {to_user}")
            print(f"Transferred ${amount} to {to_user}")
        else:
            print("Invalid recipient or insufficient funds")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def run(self):
        while True:
            if self.current_user is None:
                self.authenticate_user()
                if self.current_user is None:
                    continue

            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Transaction History")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: $"))
                self.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter the deposit amount: $"))
                self.deposit(amount)
            elif choice == "4":
                to_user = input("Enter the recipient's User ID: ")
                amount = float(input("Enter the transfer amount: $"))
                self.transfer(to_user, amount)
            elif choice == "5":
                self.transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()

