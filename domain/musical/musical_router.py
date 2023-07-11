from fastapi import APIRouter
from .models import musical

router = APIRouter(
    prefix="/musical",
)


@router.get('/list')
def musical_list():
    data = musical.getList()
    return data
