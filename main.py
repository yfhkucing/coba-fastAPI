#belajar fastAPI
#uvicorn main:app --reload
import uvicorn
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

@app.post("/")
def postBuku(results:Buku):
    return results

@app.get("/{id}")
def getBuku(id):
    iniBuku = id
    return Buku[id]

if __name__=='__main__':
    uvicorn.run(app,port=5000)