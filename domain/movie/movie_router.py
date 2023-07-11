from fastapi import APIRouter
from .models import movie

router = APIRouter(
    prefix="/movie",
)


@router.get('/list')
def movie_list():
    data = movie.getList()
    return data
