# Class
# Part 1 Вступ в ООП


# class Item:
#     def calculate_total_price(self, price, quantity):
#         return price * quantity
    
# item = Item()
# item.name = "Test name"
# item.price = 1000
# item.quantity = 90

# print(item.name)
# print(item.__dict__)

# print(item.calculate_total_price(item.price, item.quantity))

# item2 = Item()
# item2.name = "Test name2"
# item2.price = 500
# item2.quantity = 45

# print(item2.name)

# print(item2.calculate_total_price(item2.price, item.quantity))

# print(item.__dict__)


###################


# Aтрибути класу і зміні класу. Конструктор і __init__

# class Item:
#     pay_rate = 0.8 # Sum after discount in 20%
#     all_class_instance = list()
    
#     def __init__(self, name: str, price: float, quantity=0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#         Item.all_class_instance.append(self)    
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
    
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
        
#     def info(self):
#         return f'Item(name:{self.name}, price:{self.price}, quantity:{self.quantity})'

                   
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 5)


# print(item1.__dict__)
# item2.apply_discount()
# print(item2.__dict__)
# print(item2.all_class_instance)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(item1.__dict__)
# print(item2.__dict__)


############################

#  Клас метод і статичний метод

# Коли використовувати методи класу, а коли статичні методи?

# class Item:
#     @staticmethod
#     def is_integer():
#         '''
#         Це має бути щось, що має зв'язок
#         з класом, але не те, що повинно бути унікальним
#         для кожного екземпляру!
#         '''
#     @classmethod
#     def instantiate_from_something(cls):
#         '''
#         Це також має бути щось, що пов'язане
#         з класом, але зазвичай вони використовуються для
#         маніпулювання різними структурами даних для створення екземплярів
#         об'єктів
#         '''

# # ЄДИНА ВІДМІННІСТЬ МІЖ НИМИ:
# # статичні методи не передають посилання на об'єкт як перший аргумент у фоновому режимі!

# # ПРИМІТКА: Однак, їх також можна викликати з екземплярів.

# item1 = Item()
# item1.is_integer()
# item1.instantiate_from_something()


#############

# class Item:
#     pay_rate = 0.8 # Sum after discount in 20%
#     all_class_instance = list()
#     class_instances = dict()
    
#     def __init__(self, name: str, price: float, quantity=0):
        
#         assert price >= 0, f'Price {print} is nor greater or equal to zero'
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
       
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#         Item.all_class_instance.append(self)    
        
#     def calculate_total_price(self):
#         return self.price * self.quantity
    
#     def apply_discount(self):
#         self.price = self.price * self.pay_rate
        
#     def info(self):
#         return f'Item(name:{self.name}, price:{self.price}, quantity:{self.quantity})'
    
#     @classmethod
#     def all_items_info(cls):
#         return[item.info()for item in cls.all_class_instance]
        
#     @classmethod
#     def load_data_from_csv(cls):
#         with open('items.csv', 'r') as file:
#             next(file)
#             for line in file:
#                 name, price, quantity = line.strip().split(',')
#                 # cls()
#                 Item(
#                     name=name.strip('"'),
#                     price=float(price),
#                     quantity=int(quantity)
                    
#                     )
#                 item = Item(
#                     name=name.strip('"'),
#                     price=float(price),
#                     quantity=int(quantity)
#                     )
#                 Item.class_instances[name.strip('"')] = item
            
                  
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 5)

# print(item1.info())
# print(item2.info())
 
# print(item2.all_class_instance)
# print(Item.all_items_info())

# item = Item("Keyboard", 150, 7)
# item.load_data_from_csv()
# print(item.info())
# print(Item.all_items_info())


# print(Item.class_instances)
# print(Item.class_instances['Mouse'].price)

########################
#  Наслідування


# class Item:
#     pay_rate = 0.8 # Сума після знижки в 20%
#     all_class_instance = list()

#     def __init__(self, name: str, price: float, quantity=0):

#         assert price >= 0, f"Price {price} is not greater than or equal to zero"
#         assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         Item.all_class_instance.append(self)

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price = round(self.price * self.pay_rate, 2)

#     def info(self):
#         return f"Item( name:{self.name}, price:{self.price}, quantity:{self.quantity} )"
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
# class Phone(Item):
#     def __init__(self, name: str, price: float, quantity=0, brocken_phones=0):
#        super().__init__(name, price, quantity)
#        self.brocken_phones = brocken_phones
#     def info(self):
#          return f"Phone( name:{self.name}, price:{self.price}, " \
#                 f"quantity:{self.quantity}, brocken_phones: {self.brocken_phones} )"

     
# phone = Phone("Phone16", 78,945, 13)

# print(phone.info())
# phone.apply_discount() 
# print(phone.info())


# item = Item("TestItem", 9000, 3)

# print(item.info())
# item.apply_discount() 
# print(item.info())


##########################

# Інкапсуляція

# from item import Item


# item = Item('MyItem', 750)
# print(item.info())

# item.name = "OtherName"
# print(item.name)

# print(item.info())


#######################
# Поліморфізм   



# from model_6_OOP_1.phone import Phone
# from model_6_OOP_1.keyboard import Keyboard

# item1 = Keyboard('Logi', 3456)
# item1.apply_discount()
# print(item1.get_price())

# item2 = Phone('TestPhone', 1234, 1)
# item2.apply_discount()
# print(item2.get_price())