import numpy as np
from fastapi import FastAPI, File, UploadFile
import cv2
from domain.musical import musical_router
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

app.include_router(musical_router.router)
app.include_router(image_router.router)
