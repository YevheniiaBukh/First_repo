
# class Item:
#     pay_rate = 0.8 # Сума після знижки в 20%
#     all_class_instance = list()

#     def __init__(self, name: str, price: float, quantity=0):

#         assert price >= 0, f"Price {price} is not greater than or equal to zero"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

#         self.__name = name
#         self.price = price
#         self.quantity = quantity

#         Item.all_class_instance.append(self)
        
        
#     def get_name(self):
#         return self.__name

#     def set_name(self, value):
#         if len(value) > 10:
#             raise Exception("The name is to short")
#         else:
#             self.__name = value

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = round(self.price * self.pay_rate, 2)

#     def info(self):
#         return f"Item( name:{self.get_name()}, price:{self.price}, quantity:{self.quantity} )"

#     @classmethod
#     def all_items_info(cls):
#         return [item.info() for item in cls.all_class_instance]

#     @classmethod
#     def load_data_from_csv(cls):
#         with open('items.csv', 'r') as file:
#             next(file)
#             for line in file:
#                 name, price, quantity = line.strip().split(',')
#                 # cls(
#                 Item(
#                     name=name.strip('"'),
#                     price=float(price),
#                     quantity=int(quantity)
#                     )


#####################

# Поліморфізм   


# class Item:
#     pay_rate = 0.8 # Сума після знижки в 20%
#     all_class_instance = list()

#     def __init__(self, name: str, price: float, quantity=0):

#         assert price >= 0, f"Price {price} is not greater than or equal to zero"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

#         self.__name = name
#         self.__price = price
#         self.quantity = quantity

#         Item.all_class_instance.append(self)

#     def get_price(self):
#         return self.__price

#     def get_name(self):
#         return self.__name

#     def set_name(self, value):
#         if len(value) > 10:
#             raise Exception("The name is to short")
#         else:
#             self.__name = value

#     def calculate_total_price(self):
#         return self.__price * self.quantity

#     def apply_discount(self):
#         self.__price = round(self.__price * self.pay_rate, 2)

#     def info(self):
#         return f"Item( name:{self.get_name()}, price:{self.get_price()}, quantity:{self.quantity} )"

#     @classmethod
#     def all_items_info(cls):
#         return [item.info() for item in cls.all_class_instance]

#     @classmethod
#     def load_data_from_csv(cls):
#         with open('items.csv', 'r') as file:
#             next(file)
#             for line in file:
#                 name, price, quantity = line.strip().split(',')
#                 # cls(
#                 Item(
#                     name=name.strip('"'),
#                     price=float(price),
#                     quantity=int(quantity)
#                     )