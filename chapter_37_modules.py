#modules

# https://www.w3schools.com/python/python_modules.asp


# my_python_app/
# │
# ├── app/                       # Main application package
# │   ├── __init__.py            # Initializes the Python package
# │   ├── main.py                # Entry point of the application
# │   ├── module1/               # Sub-package for module1
# │   │   ├── __init__.py        # Makes module1 a Python package
# │   │   ├── class1.py          # Contains classes or functions for module1
# │   │   └── class2.py          # Additional classes or functions
# │   │
# │   ├── module2/               # Sub-package for module2
# │   │   ├── __init__.py        # Makes module2 a Python package
# │   │   ├── class3.py          # Contains classes or functions
# │   │   └── module2_utils.py   # Utility functions specific to module2
# │   │
# │   └── utils/                 # Utility module used across the application
# │       ├── __init__.py        # Makes utils a Python package
# │       ├── helper.py          # Contains common helper functions
# │       └── logger.py          # Logging utilities
# │
# ├── tests/                     # Contains unit tests
# │   ├── __init__.py
# │   ├── test_module1.py        # Test cases for module1
# │   ├── test_module2.py        # Test cases for module2
# │   └── test_utils.py          # Test cases for utility functions
# │
# ├── docs/                      # Documentation files
# │   ├── conf.py                # Sphinx configuration file
# │   └── index.rst              # Sphinx index file
# │
# ├── config/                    # Configuration files
# │   ├── __init__.py
# │   └── settings.py            # Application settings
# │
# ├── setup.py                   # Setup script for the application
# ├── requirements.txt           # Python dependencies
# └── README.md                  # Project overview and instructions


# Here's a brief explanation of each section:
# app/: This directory contains the main application logic distributed across various modules and sub-packages, module1/ and module2/.
# tests/: This directory contains unit tests for your application modules.
# docs/: This directory can contain documentation related to your project, often using tools like Sphinx.
# config/: A place for configuration files specific to environments or overall application configurations.
# setup.py: A file that describes your module details, dependencies, and other configurations to make it easier to distribute and install.
# requirements.txt: Lists all Python libraries on which your project depends.
# README.md: A markdown file that contains a high-level description of your project and how to use or install it.
# 
# This structure can scale as the complexity of the project grows and helps
# in maintaining a clean separation of concerns within the application.


# example of the local modules

# modele_one.py
def print_name(name):
    print(name)

# module_two.py
import chapter_14_functions
import chapter_14_functions as m_func # using custom name
from chapter_12_zip import my_fruits

#print(type(chapter_14_functions))
# <class 'module'>
#print(dir(chapter_14_functions))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'increase_person_age', 'my_fn', 'new_person', 'person_one', 'res', 'sum']

chapter_14_functions.sum(a = 100, b = 100)
# 200
m_func.sum(a = 100, b = 100)
# 200

print(my_fruits) #imported from chapter_12_zip 
# ['apple', 'banana', 'orange']


### Embeded Modules in Python

help('modules') # gives a list of all modules

# Модуль csv - чтение и запись CSV файлов
# Формат CSV (Comma Separated Values) является одним из самых распространенных форматов
# импорта и экспорта электронных таблиц и баз данных. CSV использовался в течение многих
# лет до того, как был стандартизирован в RFC 4180. Запоздание четко определенного стандарта
# означает, что в данных, создаваемых различными приложениями, часто существуют незначительные
# различия. Эти различия могут вызвать раздражение при обработке файлов CSV из нескольких
# источников. Тем не менее, хотя разделители, символы кавычек и некоторые другие свойства
# различаются, общий формат достаточно универсален. Значит, возможно написать один модуль,
# который может эффективно манипулировать такими данными, скрывая детали чтения и записи
# данных от программиста.

# Модуль shutil
# Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов,
# и папок. В частности, доступные здесь функции позволяют копировать, перемещать и удалять
# файлы и папки. Часто используется вместе с модулем os.

# Модуль unittest: тестируем свои программы
# Представьте, что вы написали какую-либо программу, а теперь хотите проверить, правильно ли
# она работает. Что вы для этого сделаете? Скорее всего, вы запустите её несколько раз с
# различными входными данными, и убедитесь в правильности выдаваемого ответа.
# А теперь вы что-то поменяли и снова хотите проверить корректность программы.
# Запускать ещё несколько раз? А если потом снова что-то поменяется? Нельзя ли как-то
# автоматизировать это дело?
# Оказывается, можно. В Python встроен модуль unittest, который поддерживает автоматизацию
# тестов, использование общего кода для настройки и завершения тестов, объединение тестов
# в группы, а также позволяет отделять тесты от фреймворка для вывода информации.

# Модуль subprocess
# Модуль subprocess отвечает за выполнение следующих действий: порождение новых процессов,
# соединение c потоками стандартного ввода, стандартного вывода, стандартного вывода сообщений
# об ошибках и получение кодов возврата от этих процессов.

# Модуль fractions
# Модуль fractions предоставляет поддержку рациональных чисел.

# Модуль cmath
# Модуль cmath – предоставляет функции для работы с комплексными числами.

# Модуль glob
# Модуль glob находит все пути, совпадающие с заданным шаблоном в соответствии с правилами,
# используемыми оболочкой Unix. Обрабатываются символы "*" (произвольное количество символов),
# "?" (один символ), и диапазоны символов с помощью []. Для использования тильды "~" и
# переменных окружения необходимо использовать os.path.expanduser() и os.path.expandvars().

# Модуль copy - поверхностное и глубокое копирование объектов
# Операция присваивания не копирует объект, он лишь создаёт ссылку на объект. Для изменяемых
# коллекций, или для коллекций, содержащих изменяемые элементы, часто необходима такая копия,
# чтобы её можно было изменить, не изменяя оригинал. Данный модуль предоставляет общие
# (поверхностная и глубокая) операции копирования.

# Модуль functools
# Модуль functools - сборник функций высокого уровня: взаимодействующих с другими функциями
# или возвращающие другие функции.

# Модуль os.path
# os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для
# работы с путями.

