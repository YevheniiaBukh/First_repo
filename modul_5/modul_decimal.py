# Decimal Контроль точності обчислень

# from decimal import Decimal

# first_value = 0.2 + 0.1 + 0.3 - 0.5
# print(first_value)

# second_value = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
# print(second_value)


# Налаштування точності

# from decimal import Decimal, getcontext

# value = Decimal('2')/Decimal('3')
# print(value)

# print(round(2/3,5)) # краще обирати round

# getcontext().prec = 5
# second_value = Decimal('2')/Decimal('3')
# print(second_value)

# additional_value = Decimal('1')/Decimal('3')
# print(additional_value)

# additional_value = Decimal('14')/Decimal('3')
# print(additional_value)

# additional_value = Decimal('140')/Decimal('3')
# print(additional_value)


# Округлення чисел

# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# number = Decimal('1.45')
# print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN))
# print(number.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP))
# print(Decimal('3.145678934').quantize(Decimal('1.000000')))

# print(int(number))

#####################


# Створення Decimal з дійсних чисел

# from decimal import Decimal

# number_one = 1.37
# number_two = 1.5


# first = Decimal(str(number_one)) # Перший варіант
# print(first)

# second = Decimal(str(number_two)) # Перший варіант
# print(second)

# first = Decimal.from_float(number_one) # Друщий варіант
# print(first)

# second = Decimal.from_float(number_two)
# print(second)

########################


# Генератори як функція з "yield"

# def eight_bit_counter():
#     value = 0
#     while True:
#         yield value
#         value += 1
        
# my_generator = eight_bit_counter()
# for _ in range(6):
#     print(next(my_generator))
#     print(next(my_generator))
#     print(next(my_generator))


###############


# squares_comp = (i**2 for i in range(10))
# print(squares_comp)

# for i in squares_comp:
#     print(i)
    

# for _ in range(10):
#     print(next(squares_comp))


# next(squares_comp) # error. треба обгортати в try, except


###########################


# def eight_bit_counter():
#     value = 0
#     while True:
#         yield value
#         value += 1

# my_generator = eight_bit_counter()
# for _ in range(6):
#     print(next(my_generator))


#####################

# def first_second_counter():
#     while True:
#         yield 1
#         yield 2
#         yield 3
        
# my_generator = first_second_counter()
# for _ in range(6):
#     print(next(my_generator))

###################


# def limited_generator(limit):
#     value = 0
#     while value <= limit:
#         yield value
#         value += 1
        

# for i in limited_generator(6):
#     print(i)



###################

# counter

# from collections import Counter

# def num_counter(filename, n):
#     with open(filename, 'r') as file:
#         date = file.read()
#     date_updated = [int(i) for i in date.split(',')]
#     counter = Counter(date_updated)
#     order = counter.most_common(len(counter))
#     # return [i for i in order[:n]], [i for i in order[-n:]]
#     return order[:n], order[-n:]


# most, least =  num_counter('numbers.txt', 5)
# print(f'Mosr{most} \nleast {least}')



# namedtuple

# from collections import namedtuple

# cat_info = namedtuple('Cat', ['nickname', 'age', 'owner'])
# bobs_cat = cat_info('Alex', 2, 'Bob')

# print(bobs_cat)
# print(bobs_cat.nickname)


###############


# from collections import namedtuple

# rgb = namedtuple('RGB', ['red', 'green', 'blue'])
# black = rgb(0, 0, 0)
# indigo = rgb(0, 65, 106)
# ocean_wave = rgb(143, 201, 184)


# print(black) 
# print(ocean_wave.red, indigo.blue)
# print(indigo.green - ocean_wave.green)



###################

# defaultdict

# from collections import defaultdict

# phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632', '0339993632']

# phone_operators_number = defaultdict(list)

# for phone in phone_numbers:
#     if phone.startswith('050') or phone.startswith('095'):
#         phone_operators_number['Vodafon'].append(phone)
#     if phone.startswith('067') or phone.startswith('096'):
#             phone_operators_number['Kyivstar'].append(phone)
#     if phone.startswith('063') or phone.startswith('093'):
#             phone_operators_number['Lifecell'].append(phone)
#     else:
#        phone_operators_number['Other_operators'].append(phone)

# print(phone_operators_number)
# print(phone_operators_number.get('Kyivstar'))
# print(phone_operators_number.get('Kyivstas'))
# print(phone_operators_number)



##########################3

#  deque
      
# Створення стеку
# def create_stack():
#     return []

# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0

# # Додавання елементу
# def push(stack, item):
#     stack.append(item)

# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")

# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")     
        
##########################      
 
# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue)) # ['a', 'b', 'c']

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue)) # ['b', 'c']

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0]) # ['b']

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0) # False

# # Size: Розмір черги
# print("Розмір черги:", len(queue)) # 2