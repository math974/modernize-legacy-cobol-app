#!/usr/bin/env python3

# Fichier de sauvegarde
BALANCE_FILE = "balance.json"

# Variables globales (comme en COBOL)
balance = 1000.00

# === FONCTIONS DE LOGIQUE MÉTIER (sans I/O) ===


def get_balance():
    """Retourne le solde actuel"""
    return balance


def process_amount_input(input_value):
    """
    Traite une entrée utilisateur comme le ferait COBOL PIC 9(6)V99
    Retourne le montant traité selon les règles COBOL
    """
    try:
        amount = abs(float(input_value))
        # Limite COBOL : PIC 9(6)V99 = maximum 999999.99
        max_cobol_value = 999999.99

        # En COBOL, si le nombre dépasse la limite, il est traité comme 0
        if amount > max_cobol_value:
            return 0.0
        return amount
    except (ValueError, TypeError):
        # En COBOL, les caractères non numériques sont traités comme 0
        return 0.0


def process_menu_choice(input_value):
    """
    Traite un choix de menu comme le ferait COBOL PIC 9
    Retourne le premier chiffre ou 0 si invalide
    """
    try:
        input_str = str(input_value).strip()
        if input_str and input_str[0].isdigit():
            # Comme en COBOL PIC 9, on ne garde que le premier chiffre
            return int(input_str[0])
        return 0
    except (ValueError, IndexError, AttributeError):
        return 0


def credit_operation(amount):
    """
    Effectue une opération de crédit
    Retourne True si l'opération a réussi, False sinon
    """
    global balance
    processed_amount = process_amount_input(amount)
    balance += processed_amount
    return True


def debit_operation(amount):
    """
    Effectue une opération de débit
    Retourne True si l'opération a réussi, False si fonds insuffisants
    """
    global balance
    processed_amount = process_amount_input(amount)

    if balance >= processed_amount:
        balance -= processed_amount
        return True
    return False


def reset_balance(new_balance=1000.0):
    """Remet le solde à une valeur donnée (pour les tests)"""
    global balance
    balance = new_balance


# === FONCTIONS D'INTERFACE UTILISATEUR ===


def view_balance():
    """Affiche le solde actuel"""
    print(f"Current balance: {balance:09.2f}")


def credit_account():
    """Interface pour le crédit d'un compte"""
    print("Enter credit amount: ")
    amount_input = input()
    credit_operation(amount_input)
    print(f"Amount credited. New balance: {balance:09.2f}")


def debit_account():
    """Interface pour le débit d'un compte"""
    print("Enter debit amount: ")
    amount_input = input()

    if debit_operation(amount_input):
        print(f"Amount debited. New balance: {balance:09.2f}")
    else:
        print("Insufficient funds for this debit.")


def main():
    """Fonction principale avec boucle de menu"""
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

        user_input = input().strip()
        user_choice = process_menu_choice(user_input)

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
