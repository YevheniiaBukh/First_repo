#  Бібліотека pathlib потрібна для взаємодії з файлами на вищому рівні

# from pathlib import Path

# parent_folder_path = Path('.')

# def parse_folder(path):
#     for element in path.iterdir():
#         if element.is_dir():
#             print(f"Parse folder: This is folder - {element.name}")
#         if element.is_file():
#               print(f"Parse folder: This is file - {element.name}")

# parse_folder(parent_folder_path)


############################


# Читаємо файл за допомогою бібліотеки pathlib

# Без оператора with. Необхідно закрити файл самому

# from pathlib import Path

# file_name = Path('./Temp')
# try:
#     file = open(file_name / 'jokes.txt', 'r', encoding='utf-8')
#     try:
#         while True:
#             line = file.readline() 
#             if not line:
#                 break
#             print(line, end='')
#     except OSError:
#         print('Error while reading file')
#     finally:
#         file.close()
# except OSError:
#     print('OSEroor')


#####################################


# За допомогою оператора `with`. Менше коду та зручність

# from pathlib import Path

# file_name = Path('./Temp')

# try:
#     with open(file_name / 'jokes.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line, end='')
    
# except Exception as e:
#     print(f'{e} with file')


##########################

# Використання glob


# from pathlib import Path

# file_name = Path('.')

# for elem in file_name.glob('*.py'):
#     print(elem)

# for elem in file_name.glob('*.txt'):
#      print(elem)

# for elem in file_name.glob('*txt*'):
#     print(elem)

# for elem in file_name.glob('*/'):
#     print(elem)

# for elem in file_name.glob('test*'):
#     print(elem)




#####################

# Видалення файлу 1

# from pathlib import Path

# file_name = Path('./Temp/jokes.txt')

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     pass
#     print('test')

# Видалення файлу 2

# from pathlib import Path

# file_name = Path('./Temp/jokes.txt')

# file_name.unlink(missing_ok=True)


#####################3


# Створення директорії 1

# from pathlib import Path

# new_dir = Path('ABC')

# if not new_dir.exists():
#     new_dir.mkdir()

# new_dir.mkdir(exist_ok=True)


# Створення директорії 2

# from pathlib import Path

# new_dir = Path('ABC')

# new_dir.mkdir(exist_ok=True)

########################


# Створення вкладених директорій

# from pathlib import Path

# new_dir = Path('Temp/temps/check/exist')

# new_dir.mkdir(exist_ok=True, parents=True)



###################

# Перенесення файлу

# from pathlib import Path

# old_dir = Path('test.txt')
# new_dir = Path('Temp/test_data.txt')

# old_dir.rename(new_dir)



######################


# Запис в файл

# from pathlib import Path

# file_path = Path('Temp/test_data.txt')

# data = ['first line','second line', 'third line']

#  with open(file_path, 'w', encoding='utf-8') as file: # write
#      for line in data:
#          file.write(f'{line} \n') варіант 1 
#      file.write('\n'.join(data)) варіант 2 
    
# with open(file_path, 'a') as file:
#     file.writelines(['first line\n','second line\n', 'third line\n']) # append




############################


# Робота з архівами. Заархівувати вміст папки та розархівувати

# import shutil

# archive = shutil.make_archive('backup', 'zip', 'Temp/')
# print(archive)
# shutil.unpack_archive(archive, 'New_folder')

##########################


# import shutil
# from pathlib import Path
# from random import randint, choice, choices

# MESSAGE = "Hello, Привіт"

# def get_random_filename():
#     random_value = '()+,-0123456789;=@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz' \
#                    '{}~абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
#     return ''.join(choices(random_value, k=8))


# def generate_text_files(path):
#     documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
#     with open(path / f"{get_random_filename()}.{choice(documents).lower()}", "wb") as f:
#         f.write(MESSAGE.encode())


# def generate_archive_files(path):
#     archive = ('ZIP', 'GZTAR', 'TAR')
#     shutil.make_archive(f"{path}/{get_random_filename()}", f'{choice(archive).lower()}', path)


# def generate_folders(path):
#     folder_name = ['temp', 'folder', 'dir', 'tmp', 'OMG', 'is_it_true', 'no_way', 'find_it']
#     folder_path = Path(
#         f"{path}/" + '/'.join(choices(folder_name, weights=[10, 10, 1, 1, 1, 1, 1, 1], k=randint(5, len(folder_name)))))
#     folder_path.mkdir(parents=True, exist_ok=True)


# def generate_folder_forest(path):
#     for i in range(0, randint(2, 5)):
#         generate_folders(path)


# def generate_random_files(path):
#     for i in range(3, randint(5, 7)):
#         function_list = [generate_text_files, generate_archive_files]
#         choice(function_list)(path)


# def parse_folder_recursion(path):
#     for elements in path.iterdir():
#         if elements.is_dir():
#             generate_random_files(path)
#             parse_folder_recursion(elements)


# def exist_parent_folder(path):
#     path.mkdir(parents=True, exist_ok=True)


# def file_generator(path):
#     exist_parent_folder(path)
#     generate_folder_forest(path)
#     parse_folder_recursion(path)


# if __name__ == '__main__':
#     parent_folder_path = Path("Temp")
#     file_generator(parent_folder_path)


###########################


# import sys

# # print(sys.argv[1])
# param = sys.argv[1]

# if param.find('help') != -1:
#     print("/help\n/list")
# if param == '/list':
#     print(f"List {sys.argv}")
