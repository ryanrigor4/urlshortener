from sqlite3 import Error
import sqlite3

#establishes connection with database at "directory"
def createConnection(directory):
    try:
        conn = sqlite3.connect(directory)
        print(conn)
        return conn
    except:
        print("Connection Failed!")

#fetches redirect link from "conn" using "key" as the one to search for
def fetchRedirect(conn, query, key):
    try:
        c = conn.cursor()
        c.execute(query, (key,))
        return c.fetchall()
    except Error as e:
        print(e)

#creates a table from "conn" using the query "table"
def createTable(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
        conn.commit()
    except Error as e:
        print(f"Error at createTable: {e}")

#adds link to "conn" based on "query"
def insertLink(conn, query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print(c)
    except Error as e:
        print(e)

#fetches all links based on "query"
def getLinks(conn, query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        urls = c.fetchall()
        return urls
    except Error as e:
        print(e)
#deletes all links based on "query"
def deleteLinks(conn,query):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except Error as e:
        print(e)

#deletes link from "conn" by the "key"
def deleteLink(conn,query,key):
    print(f"Query: {query}")
    try:
        c = conn.cursor()
        c.execute(query, (key,))
        conn.commit()
    except Error as e:
        print(e)