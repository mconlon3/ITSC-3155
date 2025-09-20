from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest

