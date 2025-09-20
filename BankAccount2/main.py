from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# 2 instances to test that it works
s1 = SavingsAccount("Drew", 1000, 100, 0, 1, 1.1)
s2 = SavingsAccount("Diane", 500, 100, 3, 4, 1.15)

c1 = CheckingAccount("Zach", 1000, 100, 6, 7, 500)
c2 = CheckingAccount("Morgan", 500, 100, 8, 9, 500)

s1.print_customer_information()
s2.print_customer_information()
print()

s1.calculate_interest()
s2.calculate_interest()

c1.print_customer_information()
c2.print_customer_information()
print()

c1.withdraw(350)
c2.withdraw(550)

c1.print_customer_information()
c2.print_customer_information()