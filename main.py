from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from models import MoviesModel
from random import randint
from sqlmodel import select
from schemas import MoviesSchema

app = FastAPI()

create_db_and_tables()


@app.post("/movies")
async def root(movie_data:MoviesSchema, database: SessionDep):
    movie=MoviesModel(name=movie_data.name, year=movie_data.year, length=movie_data.length, director=movie_data.director, classification=movie_data.classification, gender=movie_data.gender)
    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie


@app.get("/movies")
async def get_user(database: SessionDep):
    statement=select(MoviesModel)

    results=database.exec(statement)
    items = results.all()
    return items