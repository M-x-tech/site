import json
import uuid
from pathlib import Path
from decouple import config
from fastapi import FastAPI, HTTPException, status, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
import aiofiles

origins = [
    "http://127.0.0.1:4321",
    "http://localhost:4321",
    "https://M-x.tech",
]

root_path = "/api/v1"
app = FastAPI(root_path=root_path)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROOT_DIR = Path(config("SRV_DIR")) / "M-x-site"
ROOT_DIR.mkdir(parents=True, exist_ok=True)

COUNTER_FPATH = ROOT_DIR / "counter.txt"
COUNTER_FPATH.touch(exist_ok=True)
GUESTBOOK_FPATH = ROOT_DIR / "guestbook.jsonl"
GUESTBOOK_FPATH.touch(exist_ok=True)


# Define the Guestbook Entry model
class GuestbookEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: Optional[EmailStr] = None
    music: Optional[str] = None
    url: Optional[str] = None
    comment: str


# Endpoint for the counter
@app.get("/counter")
async def read_counter():
    try:
        async with aiofiles.open(COUNTER_FPATH, mode="r") as file:
            counter = await file.read()
            if counter == "":
                counter = 0
            new_count = int(counter) + 1
        async with aiofiles.open(COUNTER_FPATH, mode="w") as file:
            await file.write(str(new_count))
        return int(new_count)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint for adding to the guestbook
@app.post("/guestbook")
async def add_guestbook_entry(entry: GuestbookEntry):
    print(entry)
    entry_data = entry.model_dump()
    try:
        async with aiofiles.open(GUESTBOOK_FPATH, mode="a") as file:
            await file.write(f"{entry_data}\n")
        return {"entry_id": entry.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint for retrieving guestbook entries
@app.get("/guestbook")
async def read_guestbook_entries():
    entries = []
    try:
        async with aiofiles.open(GUESTBOOK_FPATH, mode="r") as file:
            async for line in file:
                entries.append(json.loads(line.strip()))
        return entries[::-1]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
