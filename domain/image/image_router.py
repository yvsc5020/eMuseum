from fastapi import APIRouter, File, UploadFile
from .models import image

router = APIRouter(
    prefix="/image",
)


@router.get('/search')
async def image_classification(file: UploadFile = File(...)):
    request_image = await file.read()
    result = image.getResult(request_image)

    return result
