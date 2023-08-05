from urllib import request
from fastapi import FastAPI
from db import conn,createTable,insertLink

requestTable = """CREATE TABLE IF NOT EXISTS url (
original text,
redirect text
);"""

createTable(requestTable)

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {"Message:", "Hello World"}

@app.post("/createLink/{original}/{redirect}")
async def create_Link(original: str, redirect: str):
    insertion = """
    INSERT INTO url(original,redirect)
    VALUES({original},{redirect})
    """
    insertLink(insertion)

@app.get("/getLinks")