from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    __tablename__ = "Movies"

    id: int = Field(primary_key=True)
    name: str
    year: int
    length: int
    director: str
    classification: str
    gender: str