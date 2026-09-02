# my_string = 'hello my liTTle friends!'

# print(my_string) # hello my liTTle friends!
# print(my_string.upper()) # HELLO MY LITTLE FRIENDS!
# print(my_string.lower()) # hello my little friends!
# print(my_string.startswith('hello')) # True
# print(my_string.startswith('hi')) # False
# print(my_string.endswith('!')) # True
# print(my_string.endswith('.')) # False
# print(my_string.title()) # Hello My Little Friends!
# print(my_string.count('e')) # 3


###############################

# Просунута робота з рядками split

# string = '   Hello, world!      \n'
# print(string)

# stripped_string = string.strip()
# print(stripped_string)


# string = 'apple, banana, orange'
# fruits = string.split(',')
# print(fruits)
# for fruit in fruits:
#     print(fruit.strip(), end=',')

# fruits = string.split(',')  
# print(fruits)

############################


# string = 'apple,banana,orange' 
# fruits = string.split(',') 

# def custom_join(iterable_object, separator):
#     return f'{separator}'.join(iterable_object)

# new_string = '-'.join(fruits)

# print( custom_join(fruits, '-'))

#########################    join

# string = 'apple,banana,orange' 


# new_string = ''.join(fruits)        # applebananaorange
# print(new_string)                   

# new_string = '\t'.join(fruits)      # apple   banana  orange
# print(new_string)  

# new_string = '-'.join(fruits)        # apple-banana-orange
# print(new_string)  

# new_string = '\n'.join(fruits)  
# print(new_string)  

##################################

# string = 'Hello world! Hello everyone!'

# find

# print(string.find('!'))
# print(string.find('@'))
# print(string.find('!', 5, 8))
# print(string.find('!', 12))
# print(string.find('!', 0, 8))
# print(string.rfind('!'))

# # index

# print(string.index('!'))
# print(string.index('@')) # error

##############################


# string = 'Hello world! Hello everyone!'
# print(test:=string.replace('world', 'Python'))


# string = '123'
# print(string.isdigit())


# string = 'abc'
# print(string.isalpha())


# string = 'abc'
# print(string.islower())

# string = 'ABC'
# print(string.isupper())

# print(test)

#######################

# string = "Ми вчимо Java? "

# print(string.replace('Java', 'Python').removesuffix('? '))


#########################

# Translate and Zip

# map = {ord('т'): 't', ord('ю'): 'yu', ord('Т'): 'T', ord('Ю'): 'YU'}

# translated = 'ТЮтютюфафафіадщщщьют.'.translate(map)
# print(translated)


##################



# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]


# MAP = {}

# for key, value in zip(symbols, code):
#     # print(key, value)
#     MAP[ord(key)] = value
#     MAP[ord(key.lower())] = value.lower()

# print(MAP)

# result = '34 DE 5C b0'.translate(MAP)
# print(result)


##############


# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# table_morze_dict = {}
# for k, v in morze_dict.items():
#     # print(k, v, sep='\t')
#     table_morze_dict[ord(k)] = v

# # for k in morze_dict:
# #     print(k, morze_dict[k], sep='\t')

# # for k in morze_dict.keys():
# #     print(k, morze_dict[k], sep='\t')
# #
# # for v in morze_dict.values():
# #     print(v, sep='\t')
# string = "Hello @world"

# result = ""

# for ch in string:
#     result = result + ch.upper().translate(table_morze_dict)

# print(result)
# result = ""

# for ch in string:
#     result = result + morze_dict.get(ch.upper(), ' ')

# print(result)

##################

# Регулярні вирази

# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."
         
# pattern = r'[0-9]+'  
# result = re.search(pattern, string)

# print(result) 
# print(result.span())  
# first, last = result.span() 
# print(string[first:last])
# print(result.group())

# result = re.findall(pattern, string)
# print(result)

# # result = re.findall(r'\s+', string)
# # print(result)

# pattern = r'\d+'
# result = re.findall(pattern, string)
# print(result)

# pattern = r'[0-9]{4}'
# result = re.findall(pattern, string)
# print(result)

# pattern = r'[0-9]{2}'
# result = re.findall(pattern, string)
# print(result)

#########################


# import re

# string = "Niels Bohr was born to Christian Bohr (1858-1911), a professor of physiology at the University of Copenhagen,"\
#          "twice a candidate for the Nobel Prize in physiology and medicine,[10] and Ellen Adler (" \
#          "1860-1930), daughter of the influential and very wealthy Jewish banker and liberal parliamentarian David " \
#          "Baruch Adler (1826—1878) and Jenny Raphael (1830-1902) of the British Jewish " \
#          "Raphael Raphael & sons[en][11] of the British Jewish banking dynasty. Bohr's parents married in 1881."

# pattern = r'\w+\.'
# result = re.findall(pattern, string)
# print(result)

# pattern = r'\w+\.$'
# result = re.findall(pattern, string)
# print(result)

# pattern = r'\w+'
# result = re.findall(pattern, string)
# print(result)

# pattern = r'[a-zA-Z]+\.'
# result = re.findall(pattern, string)
# print(result)


# pattern = r'\s+'
# result = re.findall(pattern, string)
# print(result)

# words = re.split(pattern,string)
# print(words)

# pattern = r',|&'
# words = re.split(pattern,string)
# print(words)



############################

# homework

import re

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 asf  "
]

for phone in phone_numbers:
    # cleaned_number = re.sub(r'\D', '', phone)
    cleaned_number = re.sub(r'[0-9]', '', phone)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' +cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    print(cleaned_number)