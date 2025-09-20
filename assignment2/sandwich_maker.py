
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for i in ingredients:
            if ingredients[i] > self.machine_resources[i]:
                print("Insufficient ingredients.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for i in order_ingredients:
            self.machine_resources[i] -= order_ingredients[i]
        print(f"Your {sandwich_size} sandwich is ready!")