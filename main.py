from urllib import request
from fastapi import FastAPI
from db import createTable,insertLink,getLinks,createConnection,deleteLinks
from pydantic import BaseModel
import string, random, sqlite3

dbDirectory = "/Users/ryanrigor/Documents/projects/personal/urlshortener/sqlite.db"

requestTable = """CREATE TABLE IF NOT EXISTS url (
original text,
redirect text
);"""

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#creates table and establishes connection
conn = createConnection(dbDirectory)

createTable(conn, requestTable)

class url(BaseModel):
    original: str

app = FastAPI()

@app.get("/")
async def helloWorld(url: str):
    query = ""

@app.delete("/deleteall")
async def deleteLink():
    query = f"DELETE FROM url"
    deleteLinks(conn, query)

@app.post("/createLink/")
async def create_Link(url: url):
    print(url.original)
    id = id_generator()
    insertion = f"INSERT INTO url VALUES('{url.original}','{id}')"
    insertLink(conn, insertion)

@app.get("/getLinks")
async def get_Link():
    query = "SELECT * from url"
    console = getLinks(conn, query)
    return console