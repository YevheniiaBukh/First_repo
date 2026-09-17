# If умова

# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")



# Перевірка паролю для пропуску на сайт

# entry = input("Enter password: ")

# if entry is 'test2024':
#     print('Access Granted')
# else:
#     print('Access Denied')

# if entry == 'test2024':
#     print('Access Granted')
# else:
#     print('Access Denied')



# Перевірка балансу для здійснення покупки

# balance = 0.7 + 0.6 

# if round(balance, 1) == 1.3:
#     print("Enough")
# else:
#     print("Not Enough")
    
# print(round(balance, 1))



#If...elif...else умова

# value_one = 10
# value_two = 16
# value_three = 11


# if value_one > value_two:
#     print('Value one in the biggest')
# elif value_two > value_three:
#     print('Value two in the biggest')
# else:
#     print('Value three in the biggest')



# value_x, value_y = 5, 0

# if value_x > value_y:
#     print('X > Y')
# else:
#     if value_x < value_y:
#         print("X < Y")
#     else:
#         print("X = Y")    
    


# Заміна if або оператор match

# value_x = 0

# match value_x:
#     case 0: print('Value is zero')
#     case _ if value_x % 2 == 0:
#         print(f'value_x % 2 == 0 and case is {value_x}')
#     case _ if value_x < 0:
#         print('Value is nigative')
#     case _:
#         print(value_x)




#Тернарні операції

# value_x, value_y = 5, 5

# max_value = value_x if value_x > value_y else value_y
# print(max_value)

# max_value = 'X > Y'if value_x > value_y else 'X < Y'
# print(max_value)

# max_value = 'X > Y'if value_x > value_y else 'X < Y' if value_x < value_y else 'X = Y'
# print(max_value)

# max_value = 'X = 0 or Y = 0' if value_x == 0 or value_y == 0 else "X != 0 and Y != 0"
# print(max_value)




# value_one = 13
# value_two = 10
# value_three = 13

# if value_one != value_two and value_one != value_three and value_two != value_three:
#     if value_one > value_two and value_one > value_three:
#         print('Value one in the biggest')
#     elif value_two > value_three:
#         print('Value two in the biggest')
#     else:
#         print('Value three in the biggest')
# elif value_one == value_two or value_one == value_three or value_two == value_three:
#     if value_one > value_two and value_one == value_three:
#         print('Value one and three are the biggest')
#     elif value_two > value_three and value_two == value_one:
#         print('Value two and one are the biggest')
#     elif value_three > value_one and value_two == value_three:
#         print('Value two and three are the biggest')
#     else:
#         print('All numbers equal')