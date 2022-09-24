#belajar fastAPI
#uvicorn main:app --reload
from fastapi import FastAPI
#buat bikin skema model
from pydantic import BaseModel
#serialisasi : proses convert format data ke bentuk yang bisa dikirim lewat API (kebanyakan JSON)
app = FastAPI()

dataBuku = '''{'id':'1','author':'kucing','title':'ini buku','desc':'ini deskripsi','cover_img':'linknya'}'''
#class harus huruf besar awalnya
class Buku(BaseModel):
    id:int
    author:str
    title:str
    desc:str
    cover:str

@app.get("/")
async def getBuku(id,author,title,desc,cover):
    results = {'id':id,'author':author,'title':title,'desc':desc,'cover':cover}
    return results

@app.post("/")
async def postBuku(id,author,title,desc,cover):
    results = {'id':id,'author':author,'title':title,'desc':desc,'cover':cover}
    return results