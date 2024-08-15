# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from . import models, schemas, database
# from .database import engine
# import random
# import string

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from . import models, schemas, database
from .database import engine
import random
import string

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL shortener API"}

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.post("/shorten", response_model=schemas.URL)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    short_code = generate_short_code()
    db_url = models.URL(original_url=str(url.url), short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return schemas.URL(url=url.url, short_code=short_code)

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(database.get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"url": db_url.original_url}