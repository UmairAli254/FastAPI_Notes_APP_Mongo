from fastapi import Body, FastAPI, Form, Path, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import RedirectResponse
from bson import ObjectId

app = FastAPI()
temp = Jinja2Templates(directory="view")
app.mount("/static", StaticFiles(directory="static"))

# Database setup
mongo_url = "mongodb://localhost:27017"
client = MongoClient(mongo_url)
db = client.Fast_API
collection = db.my_notes

# Schema for DB


class Db_schema(BaseModel):
 title: Optional[str] = None
 desc: Optional[str] = None


@app.get("/")
def home_page(request: Request):
 # Database Request and Getting the all records
 all_records = list(collection.find().sort({"_id": -1}))

 # Let's split the IDs of documents separately for the edit and delete button
 all_IDs = []
 for one in all_records:
  all_IDs.append(str(one["_id"]))

 return temp.TemplateResponse("home.html", {"request": request,
                                            "all_records": all_records,
                                            "all_IDs": all_IDs

                                            })


@app.post("/submit_notes")
def note_submission(note_title: str = Form(...), note_desc: str = Form(...)):

 res = collection.insert_one({
     "title": note_title,
     "desc": note_desc
 })

 if res.acknowledged != True:
  raise HTTPException(status_code=404, detail=res)

 return RedirectResponse(url="/", status_code=303)


# Patch Request
@app.post("/update_note/{note_id}")
def update_single_note(note_id: str, note_title: str = Form(...), note_desc: str = Form(...)):

 res = collection.find_one_and_update(
     {"_id": ObjectId(note_id)},
     {"$set": {
      "title": note_title,
      "desc": note_desc
      }},
     # return_document=True
 )

 return RedirectResponse(url="/", status_code=303)


@app.get("/delete_note/{note_id}")
def delete_one_note(note_id: str):
 collection.find_one_and_delete(
     {
         "_id": ObjectId(note_id)
     }
 )

 return RedirectResponse(url="/", status_code=303)
