class BankAccount:
	# Class attribute and title of bank
	bankTitle = "The Python Bank"
	
	# Instance attributes
	def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
		self.customer_name = customer_name
		self.current_balance = current_balance
		self.minimum_balance = minimum_balance
		self._account_number = account_number
		self.__routing_number = routing_number
	
	def deposit(self, count):
		self.current_balance += count
		
	def withdraw(self, count):
		if self.current_balance - count < self.minimum_balance:
			print(f"Transaction blocked on {self.customer_name}'s account. Cannot go below minimum.")
		else:
			self.current_balance -= count
	
	def print_customer_information(self):
		print(f"- {BankAccount.bankTitle} -")
		print(f"{self.customer_name}'s Account")
		print(f"Account Number: {self._account_number}")
		print(f"Current Balance: {self.current_balance}")
		print(f"Minimum Balance: {self.minimum_balance}")
	
