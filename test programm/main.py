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

command = "start"
while command != "stop":
    print("Напишите 'stop' для остановки")
    print("Напишите для вывода таблицы : "
          "'print <название таблицы> <ключ (название столбца,значение)])>'")
    print("Напишите для выбора комплектующего : "
          "'get <название таблицы> <id комплектующего>'")

    command = input()
    commandName, tableName, key = command.split() if len(command.split()) == 3 \
        else command.split() + [None]

    if commandName == "print":
        if key:
            columnName, value = key.split(',')
            key = [[columnName, value]]
            pprint(getSortedValuesFromTable(cursor, tableName, key))
        else:
            pprint(getValuesFromTable(cursor, tableName))
    elif commandName == "get":
        key = [["id", key]]
        print(*getSortedValuesFromTable(cursor, tableName, key))

connection.close()

print('Конец')
