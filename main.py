import numpy as np
from fastapi import FastAPI, File, UploadFile
import cv2
from domain.theater import theater_router
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


@app.get("/test")
async def test(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    cv2.imshow("good", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
