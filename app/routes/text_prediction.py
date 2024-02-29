
from fastapi import(
    Header,
    HTTPException,
    Depends,
    File,
    UploadFile
    )
from config.settings import Settings,get_settings
from fastapi import APIRouter
router = APIRouter()
from PIL import Image
import io
from app.main import UPLOAD_DIR
from app.helper import verify_auth
import pytesseract


@router.post("/") # http POST
async def prediction_view(file:UploadFile = File(...), authorization = Header(None), settings:Settings = Depends(get_settings)):
    verify_auth(authorization, settings)
    bytes_str = io.BytesIO(await file.read())
    try:
        img = Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid image", status_code=400)
    preds = pytesseract.image_to_string(img)
    predictions = [x for x in preds.split("\n")]
    return {"results": predictions, "original": preds}


