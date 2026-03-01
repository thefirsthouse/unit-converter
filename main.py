from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    # redirect to /weight
    return RedirectResponse("/weight", 302)


@app.get("/weight")
async def weight():
    return {"redirected": "true"}
