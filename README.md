
# 🏦 Bank Management System

A menu-driven terminal program to create bank accounts, deposit, withdraw and check balances. Data is saved to a file, so it stays between runs.

## Concepts Used
Functions • OOP (classes) • File handling • Conditions

## Requirements
- Python 3.7+
- No external libraries (uses built-in `os` only)

## How to Run
```bash
python bank_management.py
```
On Mac/Linux use `python3`.

## Menu
```
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit (saves data)
```

## How It Works
- The `Account` class stores the account number, name and balance, and has `deposit()` and `withdraw()` methods.
- Conditions stop invalid actions: negative or zero amounts, and withdrawing more than the balance.
- On startup, `load_accounts()` reads `bank_accounts.txt` and rebuilds the accounts in a dictionary.
- On exit, `save_accounts()` writes every account back to the file.
- Each account is stored as one line: `account_no,name,balance`

## Example
```
Enter choice: 1
Enter new account number: 101
Enter account holder name: Ravi
Initial deposit: 5000
Account created successfully.
```

## Tips
- Always choose **5. Exit** so your data is saved.
- Use a unique account number. Duplicates are rejected.
- Don't use commas in names, since the file is comma-separated.
- Enter numbers only for amounts.
- To reset everything, delete `bank_accounts.txt`.

## Ideas to Extend
- Add a PIN for each account
- Add a transaction history
- Add `try/except` for invalid number input
