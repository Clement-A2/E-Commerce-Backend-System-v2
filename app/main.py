from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def first_run():
    return {"message" : "E-Commerce API is running!"}