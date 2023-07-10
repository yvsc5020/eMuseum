from fastapi import APIRouter
from .models import musical

router = APIRouter(
    prefix="/musical",
)


@router.get('/list')
def theater_list():
    data = musical.getList()
    return data
