#!/usr/bin/env python3

import json

# Fichier de sauvegarde
BALANCE_FILE = "balance.json"

def load_balance():
    try:
        with open(BALANCE_FILE, 'r') as f:
            data = json.load(f)
            return data.get('balance', 1000.00)
    except FileNotFoundError:
        return 1000.00

def save_balance(balance):
    with open(BALANCE_FILE, 'w') as f:
        json.dump({'balance': balance}, f)

# Variables globales (comme en COBOL)
balance = load_balance()

def view_balance():
    print(f"Current balance: {balance:09.2f}")

def credit_account():
    global balance
    print("Enter credit amount: ")
    amount = float(input())
    balance += amount
    save_balance(balance)
    print(f"Amount credited. New balance: {balance:09.2f}")

def debit_account():
    global balance
    print("Enter debit amount: ")
    amount = float(input())
    if balance >= amount:
        balance -= amount
        save_balance(balance)
        print(f"Amount debited. New balance: {balance:09.2f}")
    else:
        print("Insufficient funds for this debit.")

def main():
    user_choice = 0
    continue_flag = "YES"
    
    while continue_flag != "NO":
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        print("Enter your choice (1-4): ", end="\n")
        
        try:
            user_choice = int(input())
        except ValueError:
            user_choice = 0
        
        if user_choice == 1:
            view_balance()
        elif user_choice == 2:
            credit_account()
        elif user_choice == 3:
            debit_account()
        elif user_choice == 4:
            continue_flag = "NO"
        else:
            print("Invalid choice, please select 1-4.")
    
    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
