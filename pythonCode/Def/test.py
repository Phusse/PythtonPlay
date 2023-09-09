class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance


def main():
    accounts = {}

    while True:
        print("\n==== Bank System ====")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            account = BankAccount(account_number, initial_balance)
            accounts[account_number] = account
            print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = accounts.get(account_number)

            if account:
                print("\nAccount Number:", account_number)
                print("Balance:", account.get_balance())

                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Back to Main Menu")

                    option = input("Enter your option: ")

                    if option == "1":
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                        print("Deposit successful!")

                    elif option == "2":
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)

                    elif option == "3":
                        break

                    else:
                        print("Invalid option!")

            else:
                print("Account not found!")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
