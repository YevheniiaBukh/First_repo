# string = 'test text'

# for chars in string:
#     print(chars)

########

# lists = [1, 2, 3, 'test text', 4, 5, 6, 7]

# for i in lists:
#     print(i)
    


########

# for i in range(len(lists)):
#     print(i, lists[i])


##########

# string_one = input('Enter string: ')
# string_two = input('Enter string to compare: ')

# for char in string_one:
#     if char not in string_two:
#         print(False)
#         break
# else:
#         print(True)



#############

        
# Number fibonachy it's importent fot IT

# num_one, num_two = 0, 1

# for _ in range(10):
#     print(num_one, end=' ')  
#     num_one, num_two = num_two, num_one + num_two
 
 
##############
 
    
# word = 'python'

# for char in word:
#     if char == 'o':
#         print('There is 0 in the word')
#         break
# else:
#     print('There is no 0 in the word')

##########

# string = 'break statement'

# for letter in string:
#     print(letter)
    
#     if letter == 'e' or letter == 's':
#        break

# print('Out of the loop')

###########


# string = 'break statement'

# for letter in string:
#     if letter == 'e' or letter == 's':
#          print(letter)
#          continue
   
#     print('spaces', letter)

# print('Out of the loop')

###########

# string = 'break statement'

# for letter in string:
#     if letter == 'e' or letter == 's':
#         pass
#     print(letter, end=' ')
# print('Out of the loop')



#############

# try:
#     value_a = input("Enter value a: ")
#     value_b = input("Enter value b: ")

#     value_x = -value_a/value_b
# except TypeError:
#     print("Type error exception block")
#     try:
#         value_x = -float(value_a)/float(value_b)
#     except ValueError:
#             print("Error !!! could not convert string to float")
#     except ZeroDivisionError:
#         print("Could not divide by zero")
   
#     else:
#         print(f'Result X equal {round(value_x, 2)}')
        
# else:
#     print(f'Result X equal {round(value_x, 2)}')
# finally:
#     print("End of calculation")


#############


# try:
#     value_a = input("Enter value a: ")
#     value_b = input("Enter value b: ")

#     value_x = -float(value_a)/float(value_b)
# except Exception as e:
#     print(e)
# else:
#     print(f'Result X equal {round(value_x, 2)}')
# finally:
#     print('End of calculation')



##########

# try:
#     pass
# except TypeError:
#     pass
# else:
#     pass
# finally:
#     pass


##########

# value_a = input("Enter value a: ")
# value_b = input("Enter value b: ")

# print(eval(f"{value_a} + {value_b}"))


# value_x = input("Enter formula: ")
# print(eval(value_x))