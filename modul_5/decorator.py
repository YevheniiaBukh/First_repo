# Функця, як об'єкту першого класу

# може бути збережена у змінній або структурі даних;

# def sum(a, b):
#     return a + b

# new_sum = sum # Зберігаємо функцію в змінній

# print(new_sum(2, 3))

####################################

# може бути передана в іншу функцію як аргумент;


# def sum(a, b):
#     return a + b

# def operation(a, b, func):
#     return func(a, b)


# print(operation(5, 3, sum))


# може бути повернута з функції як результат;

# def sum(a, b):
#     return a+b

# def minus(a, b):
#     return a-b

# def power(a):
#     return pow(a, 2)

# def operation(operator):
#     if operator == '+':
#         return sum
    
#     if operator == '-':
#         return minus
    
#     if operator == '*':
#         return power


# print(minus(7, 9))

# sum_func = operation('+')
# print(sum_func(9, 3))

# sum_func = operation('-')
# print(sum_func(9, 3))

# sum_func = operation('*')
# print(sum_func(9))


#######################


# Замикання

# message = 'Goodbye'

# def outer_func(name):
#     message = 'Hello'
#     def inner_func(message, name):
#         return f'{message} {name}'
#     return inner_func(message, name)



# print(message)
# print(outer_func('Oleh '))


######################

# factorial

# def factorial(n, cache={}):
#     if n < 0:
#         raise ValueError
    
#     def counter(n):
#         result = 1
#         for value in range(1, n+1):
#             if value in cache:
#                 result = cache[value]
#             else:
#                 result = value * cache.get(value-1, 1)
#                 cache[value] = result
#                 print('{} nor in cache {}'.format(value,result))
#         return result
    
#     return counter(n)
# print(factorial(3))
# print(factorial(6))
# print(factorial(4))

###################################

# Карування

# def greeting(variable, args):
#     print(f'function greeting with variable {variable} {args}')
    
# greeting("Test", "Passed")   


#################

# def outer_func(variable):
#     def inner_func(args):
#        print(f'function greeting with variable {variable} {args}')
#     return inner_func


# curring = outer_func('Test') 

# curring('Failed') 
# curring("Passed")


#######################
# Приклад відкладених обчислень

# def outer_func(value):
#     def inner_func(number):
#         return value * number
#     return inner_func

# multiply_five = outer_func(5)
# multiply_two = outer_func(2)

# print(multiply_five(5), multiply_five(10))
# print(multiply_two(7))


#######################

# Декоратори

# def greeting(variable):
#     print(f'Function greeting with variable {variable}')
    
# greeting('Bob')

# def bot(func):
#     def inner_func(*args,**kwargs):
#         print('Hello')
#         result = func(*args, **kwargs)
#         print('Goodbye')
#         return result
    
#     return inner_func

# bot_says = bot(greeting)
# bot_says("TEST")
############################


# Приклад без *args, **kwargs щоб краще розумілося

# def decorator(func):
#     def inner(arg_one, arg_two):
#         print('Helloooo')
#         func(arg_one, arg_two)
#         print("Goodbyyyeeeee")
#     return inner


# @decorator
# def full_name(name, surname):
#     print(f'My name is {name} {surname}')
    
# full_name('Oleh', "Osadchuk")

######################
# def outer_func(param): # Closure -> only parameters without functions
#   def inner_func(second_param):
#     return result
#   return inner_func()# function call

# def outer_func(param): # Currying -> only parameters without functions
#   def inner_func(second_param):
#     return result
#   return inner_func # function pointer call

# def outer_func(func): # Decorator -> functions and parameters to it
#   def inner_func(*args, **kwargs):
#     return result
#   return inner_func # function pointer call

##########################
# Декоратор із назвою

# def outer(some_name):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             print(f"Decorator name {some_name}")
#             return func(*args, **kwargs)
#         return inner
#     return decorator

# @outer('Check_controls')
# def adder(a, b):
#     return a+b

# print(adder(2, 5))

##################
# Lambda функція

# def number_sum(x, y):
#     return x + y


# sum = lambda x, y: x + y

# print(sum(2, 6))


#################

# Map

# names = ['oleh', 'carl', 'paul', 'candymen']

# normal_name = list(map(str.title, names))
# print(normal_name)

# def number_sqr(value):
#     return pow(value, 2)

# square_number = list(map(number_sqr, [i for i in range(10)]))
# print(square_number)

#################

# Filter

# values = [100, -3, 10, 0, -100, 33]

# positive_number = list(filter(lambda elem: elem > 0, values))
# print(positive_number)


########################

# def odd_squares(limit):
#     for value in range(limit):
#         if value % 2:
#             yield pow(value, 2)
            
# limit = 15

# get_value = filter(lambda value: bool(value % 2), map(lambda x: pow(x, 2), list(range(limit))))           
# for result in zip(get_value, odd_squares(limit)):
#     print(result[0], result[1])

######################

#  Comprehension

# # List
# print([i for i in range(10)])
# print([pow(i, i) for i in range(10) if i % 2])

# # Dict
# print({i:pow(i, 2) for i in range(10)})

# # Set
# print({i for i in range(10)})