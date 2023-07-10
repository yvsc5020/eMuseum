from fastapi import APIRouter
from .models import theater

router = APIRouter(
    prefix="/theater",
)


@router.get('/list')
def theater_list():
    data = theater.getList()
    return data


@router.get('/detail')
def theater_detail(id):
    data = theater.getDetail(id)
    return data
