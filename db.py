from calendar import c
import sqlite3
from sqlite3 import Error

conn = None
dbDirectory = "/Users/ryanrigor/Documents/projects/personal/urlshortener/sqlite.db"

def createConnection(directory):
    try:
        conn = sqlite3.connect(directory)
        print(conn)
    except:
        print("Connection Failed!")

def createTable(table):
    try:
        c = conn.cursor()
        c.execute(table)
        conn.commit()
    except Error as e:
        print(f"Error at createTable: {e}")

def insertLink(file):
    try:
        c = conn.cursor()
        c.execute(file)
        print(c)
    except Error as e:
        print(e)

def getLinks(file):
    try:
        c = conn.cursor()
    except Error as e:
        c

try:
    conn = sqlite3.connect(dbDirectory)
    print(conn)
    c = conn.cursor()
except Error as e:
    print("UNABLE TO CONNECT!")
    print(e)