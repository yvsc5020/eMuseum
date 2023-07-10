from fastapi import APIRouter
from .models import musical

router = APIRouter(
    prefix="/musical",
)


@router.get('/list')
def theater_list():
    data = musical.getList()
    return data


@router.get('/detail')
def theater_detail(id):
    data = musical.getDetail(id)
    return data
