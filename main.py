from urllib import request
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from db import createTable,insertLink,getLinks,createConnection,deleteLinks,fetchRedirect,deleteLink
from pydantic import BaseModel
import string, random, sqlite3

dbDirectory = "/Users/ryanrigor/Documents/projects/personal/urlshortener/sqlite.db"

requestTable = """CREATE TABLE IF NOT EXISTS url (
original text,
redirect text
);"""

#generates redirect key
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#creates table and establishes connection
conn = createConnection(dbDirectory)
createTable(conn, requestTable)

#request body
class url(BaseModel):
    original: str = ""
    redirect: str = ""

app = FastAPI()

@app.delete("/deleteall")
async def deleteAll():
    query = f"DELETE FROM url"
    deleteLinks(conn, query)

@app.delete("/deleteLink/{key}")
async def deleteRedirect(key: str):
    query = f"DELETE FROM URL WHERE redirect=(?)"
    deleteLink(conn, query, key)
    return key

@app.post("/createLink/")
async def create_Link(url: url):
    print(url.original)
    id = id_generator()
    insertion = f"INSERT INTO url VALUES('{url.original}','{id}')"
    insertLink(conn, insertion)
    return id

@app.get("/getLinks")
async def get_Link():
    query = "SELECT * from url"
    console = getLinks(conn, query)
    return console

@app.get("/{key}")
async def retrieveLink(key: str):
    query = f"SELECT * from url WHERE redirect=(?)"
    print(query)
    op = fetchRedirect(conn, query, key)
    return RedirectResponse(url=op[0][0]) 