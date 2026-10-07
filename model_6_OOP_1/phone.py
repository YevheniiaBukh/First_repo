# from item import Item

# class Phone(Item):
#     def __init__(self, name: str, price: float, broken_phones: int, quantity=0):
#         super().__init__(name, price, quantity)
#         self.broken_phones = broken_phones

#     def info(self):
#         return f"Phone( name:{self.get_name()}, price:{self.price}, " \
#                f"quantity:{self.quantity}, broken_phones: {self.broken_phones} )"
####################


# Поліморфізм 


# from model_6_OOP_1.item import Item

# class Phone(Item):
#     pay_rate = 0.7
#     def __init__(self, name: str, price: float, broken_phones: int, quantity=0):
#         super().__init__(name, price, quantity)
#         self.broken_phones = broken_phones
#         assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to zero"

#     def info(self):
#         return f"Phone( name:{self.get_name()}, price:{self.price}, " \
#                f"quantity:{self.quantity}, broken_phones: {self.broken_phones} )"
