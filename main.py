from fastapi import FastAPI, Depends
from utils import get_words_count
from database import SessionLocal, engine
import models
from sqlalchemy.orm import Session
import crud
import schemas
from typing import List
from fastapi.responses import JSONResponse
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import add_pagination

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

add_pagination(app)


@app.get("/get_count")
async def fetch_word_count(subject: str, number: int, db: Session = Depends(get_db)):
    result = get_words_count(subject, number)
    if result.get("error"):
        return JSONResponse(status_code=422, content=result) 
    history = crud.create_history(db, subject=subject)
    crud.create_words(db, history.id, result)

    return {"subject": subject, "result": result}

@app.get("/history", response_model=Page[schemas.PastResults])
async def get_history(db: Session = Depends(get_db)):
    # return crud.get_history(db)
    return paginate(db, crud.get_history(db))

