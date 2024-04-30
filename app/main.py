import pathlib
from fastapi import (
    FastAPI,
    Depends,
    Request,
)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .config import settings

from .routes import save_echo, text_prediction


setting = settings.get_settings()
DEBUG = settings.debug

BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"


app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)  # http GET -> JSON
def home_view(request: Request, settings: settings.Settings = Depends(setting)):
    return templates.TemplateResponse("home.html", {"request": request, "abc": 123})


app.include_router(save_echo)
app.include_router(text_prediction)
