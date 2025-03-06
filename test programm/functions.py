import sqlite3


def getValuesFromTable(cursor, tableName):
    request = f"SELECT * from {tableName}"
    cursor.execute(request)
    return cursor.fetchall()


def getSortedValuesFromTable(cursor, tableName, key):
    pass
