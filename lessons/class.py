class Pizza:

    # attributes
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, topping_input: int, gluten_free_input: bool):
        self.size = size_input
        self.toppings = topping_input
        self.gluten_free = gluten_free_input
        # this returns itself, or in this case pizza return pizza

    
    def price(self) -> float:
        """Calculates price of a pizza"""
        cost: float = 0.0
        if self.size == "large":
            cost += 6.0
        else:
            cost += 5.0

        # charge $0.75 per topping
        cost =+ 0.75*self.toppings

        # gluten free costs extra
        if self.gluten_free == True:
            cost += 1.0

        return cost
    

    def add_toppings(self, num_toppings: int) -> None:
        """Adds certain number of toppings"""
        self.toppings += num_toppings


my_pizza: Pizza = Pizza("large", 1, True)
# def price(pizza_order: Pizza) -> float:
#     """Calculates price of a pizza"""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost += 6.0
#     else:
#         cost += 5.0

#     # charge $0.75 per topping
#     cost =+ 0.75*pizza_order.toppings

#     # gluten free costs extra
#     if pizza_order.gluten_free == True:
#         cost += 1.0

#     return cost

print(my_pizza.toppings)
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())