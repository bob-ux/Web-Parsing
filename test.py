#Переменныe
# x="невероятно"
# def myFunc():
#     global x
#     x="фантастика!"

# myFunc()

# print("Python это " + x)

#Типы данных

# Тип текста:
# str (string) - строка

# Числовые типы: 
# int (integer) - целые числа
# float (float) - числа с плавающей точкой
# complex (complex) - комплексные числа

# Типы последовательностей:
# list (list) - список
# tuple (tuple) - кортеж, - неизменяемый список
# range (range) - ранжирование

# Тип отображения:
# dict (dictionary) - словарь

# Типы наборов:
# set (set) - контейнер, содержащий не повторяющиеся элементы в случайном порядке (изменяемый)
# frozenset (frozenset) - контейнер, содержащий не повторяющиеся элементы в случайном порядке (неизменяемый)

# Логический тип:
# bool (bool) - логический тип представлен двумя постоянными значениями False и True. Значения используются для представления истинности

# Бинарные типы:
# bytes (bytes) - байтовые строки
# bytearray (bytearray) - массив байт (изменяемый)
# memoryview (memoryview) - возвращает объект представления памяти

#Преобразование типа
# x=1 #int
# y=2.8 #float
# z=1j #complex

# #Конвертируем int в float 
# a=float(x)
# #Конвертируем float в int 
# b=int(y)
# #Конвертируем int в complex
# c=complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

from telnetlib import STATUS
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "http://servicenct.ac.gov.ru/references/natural-persons"
page = requests.get(url)
soup = bs(page.text, 'html.parser')
page=soup.find_all("h1")
print(page)
