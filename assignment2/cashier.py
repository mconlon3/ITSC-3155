class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        l = int(input("How many full dollars?:"))
        h = int(input("How many half dollars?:"))
        q = int(input("How many quarters?:"))
        n = int(input("How many nickels?:"))
        return (l + (h * 0.5) + (q * 0.25) + (n * 0.05))

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if(coins < cost):
            print("Sorry, that’s not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost,2)
            print(f"Here is ${change} in change.")
            return False
