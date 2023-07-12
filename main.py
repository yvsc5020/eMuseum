from fastapi import FastAPI
from domain.musical import musical_router
from domain.image import image_router
from domain.movie import movie_router
from domain.music import music_router
from domain.game import game_router
from domain.location import location_router
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(musical_router.router)
app.include_router(image_router.router)
app.include_router(movie_router.router)
app.include_router(music_router.router)
app.include_router(game_router.router)
app.include_router(location_router.router)

