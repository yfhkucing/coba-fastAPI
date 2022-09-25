#belajar fastAPI
#uvicorn main:app --reload
from fastapi import FastAPI
#buat bikin skema model
from pydantic import BaseModel
#serialisasi : proses convert format data ke bentuk yang bisa dikirim lewat API (kebanyakan JSON)
app = FastAPI()

class Buku(BaseModel):
    
