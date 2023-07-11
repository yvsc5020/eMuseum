from fastapi import APIRouter

router = APIRouter(
    prefix='/music'
)


@router.get('/list')
def music_list():
    return "good"
