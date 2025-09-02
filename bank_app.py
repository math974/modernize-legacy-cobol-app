class BankApp:
    def __init__(self, initial_balance=1000.0):
        self.balance = initial_balance

    def view_balance(self):
        return self.balance

    def credit(self, amount: float):
        if amount > 0:
            self.balance += amount
        return self.balance

    def debit(self, amount: float):
        if amount <= 0:
            return self.balance
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def exit(self):
        return "Goodbye!"
