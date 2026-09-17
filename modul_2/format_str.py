# name = 'Alisa'
# age = 30


#Пурший с з змінної message
# message = f'My name is {name}. I am {age/2} years old' 
# print(message)

#Пурший варіант форматування з змінної print
# print(f'My name is {name}. I am {age/2} years old')


#Другий  варіант форматування з змінної message
# message = 'My name is {}. I am {} years old'.format(name, age) 
# print(message) 

#Третій  варіант форматування
# message = 'My name is %s. I am %d years old' % (name, age) # S-для строки  d-для цифер 
# print(message)


# message = 'My name is ' + name + ' . I am  ' + str(age) + ' years old' 
# print(message)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# header = '|{:^15}|{:^15}|{:^15}|{:^15}|'.format('int', 'dex', 'oct','bin')
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body += '|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n'.format(num, num**2, num**3)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)

