from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), "static")

templates = Jinja2Templates("templates")


@app.get("/")
async def root():
    # redirect to /length
    return RedirectResponse("/length", 302)


@app.get("/length", response_class=HTMLResponse)
async def length(request: Request):
    return templates.TemplateResponse(request, "length.html")


@app.get("/weight", response_class=HTMLResponse)
async def weight(request: Request):
    return templates.TemplateResponse(request, "weight.html")


@app.get("/temperature")
async def temperature(request: Request):
    return templates.TemplateResponse(request, "temperature.html")
