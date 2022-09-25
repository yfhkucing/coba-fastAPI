#belajar fastAPI
#uvicorn main:app --reload
from fastapi import FastAPI
#buat bikin skema model
from pydantic import BaseModel
import json
#serialisasi : proses convert format data ke bentuk yang bisa dikirim lewat API (kebanyakan JSON)
app = FastAPI()

class Buku(BaseModel):
    id : int
    judul : str
    penulis : str
    deskripsi : str
    cover : str

with open('contohjson.json','r')

@app.post("/")
def postBuku(id,judul,penulis,deskripsi,cover):
    results = {
        "id":id,
        "judul": judul,
        "penulis": penulis,
        "deskripsi": deskripsi,
        "cover": cover
    }
    return results

@app.get("/{id}")
def getBuku(id):
    iniBuku = id
    return Buku[id]

