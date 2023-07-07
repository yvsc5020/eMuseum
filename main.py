import numpy as np
from fastapi import FastAPI, File, UploadFile
import cv2
from domain.theater import theater_router
from domain.image import image_router
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(theater_router.router)
app.include_router(image_router.router)
