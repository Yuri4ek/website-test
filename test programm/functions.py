import sqlite3

tablesNames = ['motherboards', 'processors',
               'videocards', 'rammodules',
               'storagedevices', 'coolingsystems',
               'powersupplies', 'computercases']


def getValuesFromTable(cursor, tableName):
    request = f"SELECT * FROM {tableName}"
    cursor.execute(request)
    return cursor.fetchall()


def getSortedValuesFromTable(cursor, tableName, mainKey):
    request = f"SELECT * FROM {tableName} "

    request += "WHERE "
    for i, obj in enumerate(mainKey):
        key, value = obj
        if i > 0:
            request += " AND "
        request += f"{key} == '{value}'"

    cursor.execute(request)
    return cursor.fetchall()
