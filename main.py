import os

FILE_NAME = "bank_accounts.txt"


class Account:
    def __init__(self, acc_no, name, balance=0.0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def to_line(self):
        return f"{self.acc_no},{self.name},{self.balance}\n"


def load_accounts():
    accounts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                acc_no, name, balance = line.strip().split(",")
                accounts[acc_no] = Account(acc_no, name, float(balance))
    return accounts


def save_accounts(accounts):
    with open(FILE_NAME, "w") as f:
        for acc in accounts.values():
            f.write(acc.to_line())


def create_account(accounts):
    acc_no = input("Enter new account number: ")
    if acc_no in accounts:
        print("Account already exists.")
        return
    name = input("Enter account holder name: ")
    deposit = float(input("Initial deposit: "))
    accounts[acc_no] = Account(acc_no, name, deposit)
    print("Account created successfully.")


def get_account(accounts):
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        return accounts[acc_no]
    print("Account not found.")
    return None


def main():
    accounts = load_accounts()
    while True:
        print("\n--- BANK MENU ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            acc = get_account(accounts)
            if acc:
                acc.deposit(float(input("Amount to deposit: ")))
        elif choice == "3":
            acc = get_account(accounts)
            if acc:
                acc.withdraw(float(input("Amount to withdraw: ")))
        elif choice == "4":
            acc = get_account(accounts)
            if acc:
                print(f"{acc.name}'s balance: {acc.balance}")
        elif choice == "5":
            save_accounts(accounts)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
