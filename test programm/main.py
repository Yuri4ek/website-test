from pprint import pprint
from functions import *

DBpath = '../db files/components.db'

connection = sqlite3.connect(DBpath)
cursor = connection.cursor()

print('Начало')

'''
    Основной код тут
'''
'''pprint(getSortedValuesFromTable(cursor, 'processors',
                                [['socket', 'FCLGA1851']]))'''

print("Напишите что-нибудь для начала")
while (command := input()) != "stop":
    print("Напишите 'stop' для остановки")
    print("Напишите 'print <название таблицы> <ключ (по необходимости)>' "
          "для вывода таблицы")
    print("Напишите 'get <название таблицы> <id комплектующего> "
          "для выбора комплектующего'")

connection.close()

print('Конец')
