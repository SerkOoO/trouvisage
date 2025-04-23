from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse,StreamingResponse
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from utils.opencv import findFace
import numpy as np
import cv2

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = findFace(img)
    _, encoded_img = cv2.imencode('.jpg', result)
    buffer = BytesIO(encoded_img.tobytes())

    return StreamingResponse(buffer, media_type="image/jpeg")