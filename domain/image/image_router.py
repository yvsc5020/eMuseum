from fastapi import APIRouter
from .models import image
from pydantic import BaseModel
import base64


class Item(BaseModel):
    img: str


router = APIRouter(
    prefix="/image",
)


@router.post('/search')
async def image_classification(item: Item):
    request_image = base64.b64decode(item.dict()['img'])
    result = image.getResult(request_image)

    return result
