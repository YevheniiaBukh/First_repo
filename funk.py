
# Оголошення функції де с - змінна є необовязковою

# def foo():
#     value_a = 4
#     value_b = 8
#     return value_a + value_b

# sum_value = foo()
# print(sum_value)


##################


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

# Оголошення функції де с - змінна є обовязковою

# def multiply(numbers_one, number_two, number_three):
#     print(number_three, end=' ')
#     if number_three is None:
#         return numbers_one * number_two
#     else:
#         return numbers_one * number_two * number_three

# print(multiply(2, 3, 5))
# print(multiply(2, 3)) # TypeError: multiply() missing 1 required positional argument: 'number_three'



