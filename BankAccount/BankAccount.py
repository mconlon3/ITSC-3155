class BankAccount:
	# Class attribute and title of bank
	bankTitle = "The Python Bank"
	
	# Instance attributes
	def __init__(self, customer_name, current_balance, minimum_balance):
		self.customer_name = customer_name
		self.current_balance = current_balance
		self.minimum_balance = minimum_balance
	
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
		print(f"Current Balance: {self.current_balance}")
		print(f"Minimum Balance: {self.minimum_balance}")
	
# 2 instances to test that it works
acc1 = BankAccount("Drew", 1000, 100)
acc2 = BankAccount("Diane", 500, 100)

acc1.print_customer_information()
acc2.print_customer_information()
print()

acc1.deposit(7500)
acc2.deposit(250)

acc1.print_customer_information()
acc2.print_customer_information()
print()

acc1.withdraw(250)
acc2.withdraw(675)

acc1.print_customer_information()
acc2.print_customer_information()