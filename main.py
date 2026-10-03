from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="SmartLearn AI",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "app": "SmartLearn AI"
    }
