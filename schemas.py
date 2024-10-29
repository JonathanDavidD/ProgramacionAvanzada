from pydantic import BaseModel


class MoviesSchema(BaseModel):
    name: str
    year: int
    length: int
    director: str
    classification: str
    gender: str