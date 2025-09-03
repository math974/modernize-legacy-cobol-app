#!/usr/bin/env python3

import json

# Fichier de sauvegarde
BALANCE_FILE = "balance.json"

balance = 1000.00

#def load_balance():
#    try:
#        with open(BALANCE_FILE, 'r') as f:
#            data = json.load(f)
#            return data.get('balance', 1000.00)
#    except FileNotFoundError:
#        return 1000.00
#
#def save_balance(balance):
#    with open(BALANCE_FILE, 'w') as f:
#        json.dump({'balance': balance}, f)

# Variables globales (comme en COBOL)
#balance = load_balance()

def view_balance():
    print(f"Current balance: {balance:09.2f}")

def credit_account():
    global balance
    print("Enter credit amount: ")
    amount = abs(float(input()))
    
    # Limite COBOL : PIC 9(6)V99 = maximum 999999.99
    MAX_COBOL_VALUE = 999999.99
    
    # Vérifier si l'amount ou le nouveau solde dépassent la limite COBOL
    if amount > MAX_COBOL_VALUE or (balance + amount) > MAX_COBOL_VALUE:
        # En COBOL, l'opération ne se fait pas en cas d'overflow
        # On n'affiche rien et on ne modifie pas le solde
        return
    
    balance += amount
    #save_balance(balance)
    print(f"Amount credited. New balance: {balance:09.2f}")

def debit_account():
    global balance
    print("Enter debit amount: ")
    amount = abs(float(input()))
    
    # Limite COBOL : PIC 9(6)V99 = maximum 999999.99
    MAX_COBOL_VALUE = 999999.99
    
    # Vérifier si l'amount dépasse la limite COBOL
    if amount > MAX_COBOL_VALUE:
        # En COBOL, l'opération ne se fait pas en cas d'overflow
        # On n'affiche rien et on ne modifie pas le solde
        return
    
    if balance >= amount:
        balance -= amount
        #save_balance(balance)
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
            input_str = input().strip()
            if input_str and input_str[0].isdigit():
                # Comme en COBOL PIC 9, on ne garde que le premier chiffre
                user_choice = int(input_str[0])
            else:
                user_choice = 0
        except (ValueError, IndexError):
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
