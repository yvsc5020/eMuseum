from fastapi import APIRouter
from .models import location

router = APIRouter(
    prefix="/location",
)


@router.get('/search')
async def location_list():
    data = location.getList()
    return data
