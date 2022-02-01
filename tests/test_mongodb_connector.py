from mongodb_connector import __version__

import sqlite3
from mongodb_connector import connect
from pymongo import MongoClient

def test_version():
    assert __version__ == '0.1.0'


def test_mongodb_connector():
    # connection = sqlite3.connect(':memory:')
    # cursor = connection.cursor()
    # cursor.execute("CREATE TABLE IF NOT EXISTS FOO (ID INTEGER PRIMARY KEY, NAME TEXT)")
    # cursor.execute("INSERT INTO FOO (ID,NAME) VALUES (?,?)", (1,"First"))
    # cursor.execute("SELECT * FROM FOO")
    # result = cursor.fetchall()
    # print(result)
    # connection.close()

    connection = connect("localhost", 27017, None, None, "testdb")
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM csv WHERE year >= 10")
    cursor.execute("INSERT INTO csv (name,year) VALUES (\"Mike\",30)")
    obj = cursor.fetchall()
    print(obj)
    connection.close()

    # # client = MongoClient("mongodb://localhost:27017/")
    # # collection = client["testdb"]["csv"]
    # # obj = collection.find({'year':{'$gt':1}})
    # # print(obj)

    # for d in obj:
    #     print(d)

"""
# 対応するSQL例
* 日付型はサポートされていない
* SELECT
    * DISTINCT Keyword 
    * FROM expression
    * WHERE expression
    (* ORDER BY expression)
    (* GROUP BY expression)
    (* LIMIT expression)
    (* OFFSET expression)
    (* HAVING expression)
* INSERT INTO table_name (column_name, column_name, ...) VALUES (?,?)
* UPDATE table SET () WHERE expression 
* DELETE FROM table_name WHERE expression
* CREATE TABLE table_name (column_name column_type, column_name column_type, ...)
    (* PRIMARY KEY will not be supported.)
* DROP TABLE table_name
"""

if __name__ == '__main__':
    test_mongodb_connector()