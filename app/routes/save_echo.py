
from fastapi import(
    HTTPException,
    Depends,
    File,
    UploadFile
    )
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from config.settings import Settings,get_settings
from app.main import UPLOAD_DIR
router = APIRouter()
from PIL import Image
import pathlib
import io
import uuid

@router.post("/img-echo/", response_class=FileResponse) # http POST
async def img_echo_view(file:UploadFile = File(...), settings:Settings = Depends(get_settings)):
    if not settings.echo_active:
        raise HTTPException(detail="Invalid endpoint", status_code=400)
    UPLOAD_DIR.mkdir(exist_ok=True)
    bytes_str = io.BytesIO(await file.read())
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid image", status_code=400)
    fname = pathlib.Path(file.filename)
    fext = fname.suffix # .jpg, .txt
    dest = UPLOAD_DIR / f"{uuid.uuid1()}{fext}"
    img.save(dest)
    return dest
