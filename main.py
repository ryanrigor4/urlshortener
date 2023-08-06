from urllib import request
from fastapi import FastAPI
from db import createTable,insertLink,getLinks,createConnection
from pydantic import BaseModel

dbDirectory = "/Users/ryanrigor/Documents/projects/personal/urlshortener/sqlite.db"
requestTable = """CREATE TABLE IF NOT EXISTS url (
original text,
redirect text
);"""

#creates table and establishes connection
conn = createConnection(dbDirectory)
createTable(conn, requestTable)

class url(BaseModel):
    original: str
    redirect: str

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {"Message:", "Hello World"}

@app.post("/createLink/")
async def create_Link(url: url):
    print(url.original)
    print(url.redirect)
    insertion = f"INSERT INTO url VALUES('{url.original}','{url.redirect}')"
    insertLink(conn, insertion)
    

@app.get("/getLinks")
async def get_Link():
    query = "SELECT * from url"
    console = getLinks(conn, query)
    return console