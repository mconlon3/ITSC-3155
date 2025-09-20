import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    on = 1
    while(on):
        option = input("What would you like? (small/ medium/ large/ off/ report): ")
        match option:
            case "off":
                print("Powered off.")
                on = 0
            case "small":
                if sandwich_maker_instance.check_resources(recipes["small"]["ingredients"]):
                    pay = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(pay, recipes["small"]["cost"]):
                        sandwich_maker_instance.make_sandwich("small", recipes["small"]["ingredients"])
            case "medium":
                if sandwich_maker_instance.check_resources(recipes["medium"]["ingredients"]):
                    pay = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(pay, recipes["medium"]["cost"]):
                        sandwich_maker_instance.make_sandwich("medium", recipes["medium"]["ingredients"])
            case "large":
                if sandwich_maker_instance.check_resources(recipes["large"]["ingredients"]):
                    pay = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(pay, recipes["large"]["cost"]):
                        sandwich_maker_instance.make_sandwich("large", recipes["large"]["ingredients"])
            case "report":
                print("- INVENTORY -")
                print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
                print(f"Ham: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
                print(f"Cheese: {sandwich_maker_instance.machine_resources['bread']} ounce(s)")
            case _:
                print("Invalid option!")

if __name__=="__main__":
    main()

