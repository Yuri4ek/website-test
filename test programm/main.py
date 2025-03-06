from pprint import pprint
from functions import *

DBpath = '../db files/components.db'

connectino = sqlite3.connect(DBpath)
cursor = connectino.cursor()

'''
    Основной код тут
'''
pprint(getValuesFromTable(cursor, "processors"))

connectino.close()

print('Начало')