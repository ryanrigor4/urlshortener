from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from db import insertLink,getLinks,createConnection,deleteLinks,fetchRedirect,deleteLink
from pydantic import BaseModel
import string, random, os
from dotenv import load_dotenv
from generator import id_generator

#loads env file and stores DB_DIRECTORY into variable dbDriectroy
load_dotenv()
dbDirectory = os.getenv('DB_DIRECTORY')

app = FastAPI()

#request body
class url(BaseModel):
    original: str = ""
    redirect: str = ""

@app.delete("/deleteall")
async def deleteAll():
    conn = createConnection(dbDirectory)
    query = f"DELETE FROM url"
    deleteLinks(conn, query)
    conn.close()

@app.delete("/deleteLink/{key}")
async def deleteRedirect(key: str):
    conn = createConnection(dbDirectory)
    query = f"DELETE FROM URL WHERE redirect=(?)"
    deleteLink(conn, query, key)
    conn.close()
    return key

@app.post("/createLink/")
async def create_Link(url: url):
    conn = createConnection(dbDirectory)
    print(url.original)
    id = id_generator()
    insertion = f"INSERT INTO url VALUES('{url.original}','{id}')"
    insertLink(conn, insertion)
    conn.close()
    return id

@app.get("/getLinks")
async def get_Link():
    conn = createConnection(dbDirectory)
    query = "SELECT * from url"
    console = getLinks(conn, query)
    conn.close()
    return console

@app.get("/{key}")
async def retrieveLink(key: str):
    conn = createConnection(dbDirectory)
    query = f"SELECT * from url WHERE redirect=(?)"
    print(query)
    op = fetchRedirect(conn, query, key)
    conn.close()
    return RedirectResponse(url=op[0][0]) 