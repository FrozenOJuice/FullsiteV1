from fastapi import FastAPI, HTTPException
from backend.data_manager import load_movies
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "root route!!"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/movies")
async def get_movies():
    return load_movies()

@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    movies = load_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

