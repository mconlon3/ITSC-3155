from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.limit = limit

    # Transfer limit is in BankAccount already