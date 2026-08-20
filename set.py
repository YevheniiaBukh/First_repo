# my_set = set('hi there!') # Не рекомендується використовувати строки
# print(my_set)

# my_set = {4, 6, 'test','Python', 100}
# print(my_set)

# my_set.add('Test')
# print(my_set)

# my_set.remove(6)
# print(my_set)

# my_set.discard('Test') # М'яке видалиня
# print(my_set)


# list_data_one = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]
# list_data_two = [11, 1, 21, 31, 15, 8, 13, 21, 7, 15, 101]

# print(list(set(list_data_one) & set(list_data_two))) # in first and in second &(and)
# print(list(set(list_data_one) | set(list_data_two))) # in first or in second |(or)
# print(list(set(list_data_one) - set(list_data_two))) # in first and not in second -(minus)
# print(list(set(list_data_one) ^ set(list_data_two))) # in first and not in second + in second and not in first
 
# list_data_one = [1, 1, 2, 3, 5, 8, 13]
# list_data_two = [11, 1, 21, 31, 15, 8]

# print(len(list_data_one) == len(set(list_data_one)))
# print(len(list_data_two) == len(set(list_data_two)))