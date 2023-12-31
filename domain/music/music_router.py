from fastapi import APIRouter
from .models import music

router = APIRouter(
    prefix='/music'
)


@router.get('/list')
def music_list():
    data = music.getList()
    return data
