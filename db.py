from sqlite3 import Error
import sqlite3

def createConnection(directory):
    try:
        conn = sqlite3.connect(directory)
        print(conn)
        return conn
    except:
        print("Connection Failed!")

def fetchRedirect(conn, query, key):
    try:
        c = conn.cursor()
        c.execute(query, (key,))
        return c.fetchall()
    except Error as e:
        print(e)

def createTable(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
        conn.commit()
    except Error as e:
        print(f"Error at createTable: {e}")

def insertLink(conn, query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print(c)
    except Error as e:
        print(e)

def getLinks(conn, query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        urls = c.fetchall()
        return urls
    except Error as e:
        print(e)

def deleteLinks(conn,query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)

        
def deleteLink(conn,query,key):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query, (key,))
        conn.commit()
    except Error as e:
        print(e)