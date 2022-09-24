#belajar fastAPI
#uvicorn main:app --reload
from fastapi import FastAPI
#serialisasi : proses convert format data ke bentuk yang bisa dikirim lewat API (kebanyakan JSON)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/haloo")
def aaaa():
    return {"Halo":"dek"}