### Data ###
### Marcus ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in ingredients:
            if ingredients[i] > self.machine_resources[i]:
                print("Insufficient ingredients.")
                return False
        return True
    
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
            
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for i in order_ingredients:
            self.machine_resources[i] -= order_ingredients[i]
        print(f"Your {sandwich_size} sandwich is ready!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

sm = SandwichMachine(resources)
on = 1
while(on):
    option = input("What would you like? (small/ medium/ large/ off/ report): ")
    match option:
        case "off":
            print("Powered off.")
            on = 0
        case "small":
            if sm.check_resources(recipes["small"]["ingredients"]):
                pay = sm.process_coins()
                if sm.transaction_result(pay, recipes["small"]["cost"]):
                    sm.make_sandwich("small", recipes["small"]["ingredients"])
        case "medium":
            if sm.check_resources(recipes["medium"]["ingredients"]):
                pay = sm.process_coins()
                if sm.transaction_result(pay, recipes["medium"]["cost"]):
                    sm.make_sandwich("medium", recipes["medium"]["ingredients"])
        case "large":
            if sm.check_resources(recipes["large"]["ingredients"]):
                pay = sm.process_coins()
                if sm.transaction_result(pay, recipes["large"]["cost"]):
                    sm.make_sandwich("large", recipes["large"]["ingredients"])
        case "report":
            print("- INVENTORY -")
            print(f"Bread: {sm.machine_resources['bread']} slice(s)")
            print(f"Ham: {sm.machine_resources['bread']} slice(s)")
            print(f"Cheese: {sm.machine_resources['bread']} ounce(s)")
        case _:
            print("Invalid option!")




