
# Оголошення функції де с - змінна є необовязковою

# def foo():
#     value_a = 4
#     value_b = 8
#     return value_a + value_b

# sum_value = foo()
# print(sum_value)


##################
# Вигляд по всім вимогам з використанням вхідних параметрів

# def add(value_one: int, value_two: int)-> int:
#     """
#     Function af adding two numbers

#     Input:
#     :param value_one: integer
#     :param value_two: integer

#     Output:
#     :return: integer
#     """
#     sum_of_two_numbers = value_one + value_two
#     return sum_of_two_numbers
    

# result: int = add(2, 4)
# print(result)


#################


# Оголошення функції де с - змінна є необовязковою

# def multiply(numbers_one, numbers_two, numbers_three=None):
#     print(numbers_three, end=' ')
#     if numbers_three is None:
#         return numbers_one * numbers_two
#     else:
#         return numbers_one * numbers_two * numbers_three
    
    
    
# print(multiply(2, 3))
# print(multiply(2, 3, 5))



#######################

# Оголошення функції де с - змінна є необовязковою

# def multiply(numbers_one, number_two, number_three=None):
#     print(number_three, end=' ')
#     if number_three is None:
#         return numbers_one * number_two
#     else:
#         return numbers_one * number_two * number_three

# print(multiply(2, 3, 5))
# print(multiply(2, 3)) # TypeError: multiply() missing 1 required positional argument: 'number_three'


########################

# Оголошення функції де с - змінна є обовязковою

# def add(numbers_one, numbers_two):
#     return numbers_one + numbers_two

# print(add(3, 4))
# print(add(2, 3, 4)) -> TypeError: add() takes 2 positional arguments but 3 were given

# def sum_of_all_numbers(*numbers): #args -> tuple (2,3,4,5,6,7,7)
#     sum = 0
#     for value in numbers:
#         sum += value
#     return sum


# print(sum_of_all_numbers(2,3,4,5,6,7,7))
        
        
###################### 

# Розрахунок суми всіх чисел, що подаються через *args

# def sum_of_all_numbers(*numbers): #args -> tuple (2,3,4,5,6,7,7)
#     sum = 0
#     for value in numbers:
#         try:
#             sum += float(value)
#         except TypeError:
#             continue
#         except ValueError:
#             continue
#     return sum


# print(sum_of_all_numbers(1,2,3,4,5,1000,6,7,8,9,0,7.7, 'true', False, 90, -100,sum([1,2,3,4,99])))


######################################3


# Виористання множини іменних параметрів

# def gretting(**kwargs):  #  -> kwargs = {'key': value, ..... 'key_n': value_n}
#     print(kwargs)
#     name = kwargs.get("name", "Unknown")
#     age = kwargs.get("age", 18)
#     print(f"Hello {name}, you are {age} years old")

# gretting(name="Oleh")
# gretting(name="Oleh", age=100)


######################

# def fnc(a, **b):
#     ...
    
# test = {'k': 100}
# for i in test:
#     print(test[i])

############

# def fnc(a, **b):
#     sum = 0
#     for k in b:
#         sum += b[k]
#     return sum

# result = fnc(10, k=1, m=2, n=3, j=4)
# print(result)

###############


# Оголошення функції з використанням всіх видів передачі вхідних параметрів


# def print_input(value, *transport, **text):
#     print(value)
#     print(transport)
#     print(text)
#     print(text['may']/9)
    
# print_input(78, 246, 'qwerty', 'iuagfioaggli;as', 346346346, 50, hello="Python", may=45)
    
##################
# Local зміна a i b

# def foo():
#     a = 4
#     b = 8
#     print(f"a = {a}, b = {b}")
#     return a+b

# print(foo())


##################
# Global зміна x

# x = 10
# print(x)

# def foo():
#     global x
#     print(x)
#     x = 5
#     print(x)


# foo()
# print(x)

################
#Nonlocal зміна password

# password = 1234

# def security(passwd):
#     def divide():
#         nonlocal passwd
#         print(passwd)
#         return passwd / 2
#     return divide()

# print(security(password))
        
    
#####################  

# Рекурсія
# Example 1 fibinachi and ternarni operator
# def fibonachi(number):
#     return number if number == 0 or number == 1 else fibonachi(number-2) + fibonachi(number-1)
    
# print(fibonachi(10))   
    
# Example 2

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent-1)
    
# print (pow(2, 3))
# print(power(2, 3))
        
##############################

# Використовуйте len() для визначення довжини рядка. Для створення рядка з пробілів використовуйте " " * кількість_пробілів
# def format_string(string, length):
#     if len(string) > length:
#         return string
#     else:
#         total_spaces = length - len(string)
#         space_left = total_spaces // 2
#         space_right = total_spaces - space_left
#         return " " * space_left + string + " " * space_right
        
#############################

# Записати у довідник кількість кожного елемента, який передається у строці        
    
# def char_counter(sentence): # Приймає на вхід строку
#     operator_dict = dict() # створюєио пустий словник, ключ -- буква, значення -- к-ть повторень

#     for char in sentence: # проходимось по всіх елементах строки
#         if char not in operator_dict.keys(): # перевіряємо чи конкретоний строки вже є в словнику
#             operator_dict[char] = 1 # добавляємо в словник і присвоюємо 1 як повторення
#         else: # в іншому випадку
#             operator_dict[char] += 1 # збільшуємо значення цього елементу на 1
#     return operator_dict # повертаємо словник

# user_input = input("Enter sentence: ")

# print(char_counter(user_input))
# print(char_counter(user_input).keys())
# print(char_counter(user_input).values())

##########################

# Програма загадує ціле число від 0 до n, де n - переданий у функцію параметр. 
# Користувач намагається відгадати загадане число. 
# Якщо користувач назвав занадто велике число, функція повинна відповісти 'Smaller'. 
# Якщо він назвав занадто маленьке число, функція повинна 'Larger'.
# Якщо користувач вгадав число, функція повинна відповісти 'You win!' і говорить за скільки спроб він вгадав

# def predict_number(number): # створюємо функцію, яка приймає число на вхід для діапазону чисел
#     count = 0 # лічильник для спроб вгадування числа
#     goal = randint(0, number) # генеруємо число від 0 до аргументу функції

#     while True: # вічний
#         user_input = int(input(f"Guess the number form 0 to {number}: ")) # користувач вводить число з підказкою у вигляді діапазону
#         count += 1 # При кожному ведені лічилдьник збільшується на один

#         if user_input > goal: # Якщо число введегне є більше за генероване повідомляємо користувача
#             print("Smaller")
#         elif user_input < goal: #  Якщо число введегне є менше за генероване повідомляємо користувача
#             print("Larger")
#         else: #  Якщо число введегне рівне генерованому повідомляємо користувача і перериваємо цикл
#             print(f"You win! Number of attempts {count}")
#             break

# predict_number(10)


################################


