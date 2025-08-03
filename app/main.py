# app/main.py
import os
import io
import cv2
import numpy as np
from enum import Enum
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.utils import detect_and_draw_box

app = FastAPI(title="Deploying an ML model with FastAPI")

class Model(str, Enum):
    mobilenet = "mobilenet"

@app.get("/")
def home():
    return {"message": "Welcome to the ML model deployment server! Now head over to /docs"}

@app.post("/predict")
def prediction(model: Model, file: UploadFile = File(...)):
    filename = file.filename
    if not filename.split(".")[-1].lower() in ("jpg", "jpeg", "png"):
        raise HTTPException(status_code=415, detail="Unsupported file provided")

    image_stream = io.BytesIO(file.file.read())
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if model == Model.mobilenet:
        image = detect_and_draw_box(image)
    else:
        raise HTTPException(status_code=400, detail="Model not supported")

    out_path = f"app/static/images_uploaded/{filename}"
    cv2.imwrite(out_path, image)
    return StreamingResponse(open(out_path, "rb"), media_type="image/jpeg")
