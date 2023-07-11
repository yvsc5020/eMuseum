from fastapi import APIRouter
from .models import game

router = APIRouter(
    prefix='/game'
)


@router.get('/list')
def game_list():
    data = game.getList()
    return data
