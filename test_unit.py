#!/usr/bin/env python3

import pytest
import main

class TestBusinessLogic:
    """Tests des fonctions de logique métier (sans I/O)"""
    
    def setup_method(self):
        """Réinitialise le solde avant chaque test"""
        main.reset_balance(1000.0)
    
    def test_get_balance(self):
        """Test de récupération du solde"""
        assert main.get_balance() == 1000.0
        
        main.reset_balance(500.0)
        assert main.get_balance() == 500.0
    
    def test_reset_balance(self):
        """Test de réinitialisation du solde"""
        main.reset_balance(2500.0)
        assert main.get_balance() == 2500.0
        
        main.reset_balance()  # Valeur par défaut
        assert main.get_balance() == 1000.0

class TestAmountProcessing:
    """Tests de traitement des montants selon les règles COBOL"""
    
    def test_process_amount_valid_numbers(self):
        """Test avec des nombres valides"""
        assert main.process_amount_input("100") == 100.0
        assert main.process_amount_input("100.50") == 100.50
        assert main.process_amount_input("0") == 0.0
        assert main.process_amount_input("999999.99") == 999999.99
    
    def test_process_amount_negative_numbers(self):
        """Test avec des nombres négatifs (deviennent positifs)"""
        assert main.process_amount_input("-100") == 100.0
        assert main.process_amount_input("-50.25") == 50.25
    
    def test_process_amount_overflow(self):
        """Test avec des nombres trop grands (overflow -> 0)"""
        assert main.process_amount_input("1000000") == 0.0  # > 999999.99
        assert main.process_amount_input("10000000000000000000") == 0.0
        assert main.process_amount_input("999999.999") == 0.0  # > 999999.99
    
    def test_process_amount_invalid_input(self):
        """Test avec des entrées invalides (-> 0)"""
        assert main.process_amount_input("abc") == 0.0
        assert main.process_amount_input("") == 0.0
        assert main.process_amount_input("xyz123") == 0.0
        assert main.process_amount_input("12.34.56") == 0.0
        assert main.process_amount_input(None) == 0.0
    
    def test_process_amount_edge_cases(self):
        """Test des cas limites"""
        assert main.process_amount_input("999999.98") == 999999.98
        assert main.process_amount_input("1000000.00") == 0.0
        assert main.process_amount_input("0.01") == 0.01

class TestMenuProcessing:
    """Tests de traitement des choix de menu selon les règles COBOL PIC 9"""
    
    def test_process_menu_valid_choices(self):
        """Test avec des choix valides"""
        assert main.process_menu_choice("1") == 1
        assert main.process_menu_choice("2") == 2
        assert main.process_menu_choice("3") == 3
        assert main.process_menu_choice("4") == 4
    
    def test_process_menu_first_digit_only(self):
        """Test que seul le premier chiffre est pris (comme COBOL PIC 9)"""
        assert main.process_menu_choice("100") == 1
        assert main.process_menu_choice("2000") == 2
        assert main.process_menu_choice("3.14") == 3
        assert main.process_menu_choice("4abc") == 4
        assert main.process_menu_choice("567") == 5
    
    def test_process_menu_invalid_choices(self):
        """Test avec des choix invalides (-> 0)"""
        assert main.process_menu_choice("abc") == 0
        assert main.process_menu_choice("") == 0
        assert main.process_menu_choice("xyz") == 0
        assert main.process_menu_choice(" ") == 0
        assert main.process_menu_choice(None) == 0
    
    def test_process_menu_edge_cases(self):
        """Test des cas limites"""
        assert main.process_menu_choice("0") == 0
        assert main.process_menu_choice("9") == 9
        assert main.process_menu_choice(" 1 ") == 1  # Avec espaces
        assert main.process_menu_choice("1.0") == 1

class TestCreditOperation:
    """Tests des opérations de crédit"""
    
    def setup_method(self):
        """Réinitialise le solde avant chaque test"""
        main.reset_balance(1000.0)
    
    def test_credit_valid_amounts(self):
        """Test de crédit avec des montants valides"""
        assert main.credit_operation("100") == True
        assert main.get_balance() == 1100.0
        
        assert main.credit_operation("50.25") == True
        assert main.get_balance() == 1150.25
    
    def test_credit_zero_amount(self):
        """Test de crédit avec montant zéro"""
        assert main.credit_operation("0") == True
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_credit_negative_amount(self):
        """Test de crédit avec montant négatif (devient positif)"""
        assert main.credit_operation("-100") == True
        assert main.get_balance() == 1100.0
    
    def test_credit_invalid_amount(self):
        """Test de crédit avec montant invalide (traité comme 0)"""
        assert main.credit_operation("abc") == True
        assert main.get_balance() == 1000.0  # Pas de changement
        
        assert main.credit_operation("") == True
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_credit_overflow_amount(self):
        """Test de crédit avec montant overflow (traité comme 0)"""
        assert main.credit_operation("10000000000000000000") == True
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_credit_max_valid_amount(self):
        """Test de crédit avec le montant maximum valide"""
        main.reset_balance(0.0)
        assert main.credit_operation("999999.99") == True
        assert main.get_balance() == 999999.99

class TestDebitOperation:
    """Tests des opérations de débit"""
    
    def setup_method(self):
        """Réinitialise le solde avant chaque test"""
        main.reset_balance(1000.0)
    
    def test_debit_valid_amounts(self):
        """Test de débit avec des montants valides"""
        assert main.debit_operation("100") == True
        assert main.get_balance() == 900.0
        
        assert main.debit_operation("50.25") == True
        assert main.get_balance() == 849.75
    
    def test_debit_zero_amount(self):
        """Test de débit avec montant zéro"""
        assert main.debit_operation("0") == True
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_debit_negative_amount(self):
        """Test de débit avec montant négatif (devient positif)"""
        assert main.debit_operation("-100") == True
        assert main.get_balance() == 900.0
    
    def test_debit_insufficient_funds(self):
        """Test de débit avec fonds insuffisants"""
        assert main.debit_operation("2000") == False
        assert main.get_balance() == 1000.0  # Pas de changement
        
        assert main.debit_operation("1000.01") == False
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_debit_exact_balance(self):
        """Test de débit avec le montant exact du solde"""
        assert main.debit_operation("1000") == True
        assert main.get_balance() == 0.0
    
    def test_debit_invalid_amount(self):
        """Test de débit avec montant invalide (traité comme 0)"""
        assert main.debit_operation("abc") == True
        assert main.get_balance() == 1000.0  # Pas de changement
        
        assert main.debit_operation("") == True
        assert main.get_balance() == 1000.0  # Pas de changement
    
    def test_debit_overflow_amount(self):
        """Test de débit avec montant overflow (traité comme 0)"""
        assert main.debit_operation("10000000000000000000") == True
        assert main.get_balance() == 1000.0  # Pas de changement

class TestCobolCompatibility:
    """Tests de compatibilité avec le comportement COBOL"""
    
    def setup_method(self):
        """Réinitialise le solde avant chaque test"""
        main.reset_balance(1000.0)
    
    def test_cobol_pic_9_6_v_99_limits(self):
        """Test des limites PIC 9(6)V99"""
        # Valeurs à la limite
        assert main.process_amount_input("999999.99") == 999999.99
        assert main.process_amount_input("999999.98") == 999999.98
        
        # Valeurs qui dépassent
        assert main.process_amount_input("1000000.00") == 0.0
        assert main.process_amount_input("999999.999") == 0.0
    
    def test_cobol_pic_9_menu_behavior(self):
        """Test du comportement PIC 9 pour les choix de menu"""
        # Premier chiffre seulement
        assert main.process_menu_choice("123") == 1
        assert main.process_menu_choice("456") == 4
        assert main.process_menu_choice("789") == 7
        
        # Caractères non numériques
        assert main.process_menu_choice("a1") == 0
        assert main.process_menu_choice("1a") == 1
    
    def test_multiple_operations_sequence(self):
        """Test d'une séquence d'opérations multiples"""
        # Crédit puis débit
        main.credit_operation("500")
        assert main.get_balance() == 1500.0
        
        main.debit_operation("200")
        assert main.get_balance() == 1300.0
        
        # Débit impossible
        result = main.debit_operation("2000")
        assert result == False
        assert main.get_balance() == 1300.0  # Pas de changement
        
        # Crédit avec overflow (traité comme 0)
        main.credit_operation("10000000000000000000")
        assert main.get_balance() == 1300.0  # Pas de changement

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=main", "--cov-report=term-missing"])