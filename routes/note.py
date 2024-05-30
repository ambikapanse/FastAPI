from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Depends
from models.note import Note
from fastapi.templating import Jinja2Templates
from config.db import conn
from schemas.note import noteEntity, notesEntity


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "title": doc["title"],
            "desc": doc["desc"],
            "urgent": doc["urgent"],
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["urgent"] = True if formDict.get("urgent") == "on" else False
    result = conn.notes.notes.insert_one(formDict)
    return {"Success": True}
