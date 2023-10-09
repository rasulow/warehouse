from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from core import Base, engine, get_db
import models as _mod


app = FastAPI()


origins = ["*"]
methods = ["*"]
headers = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers,
)

Base.metadata.create_all(engine)


@app.get('/')
async def get_home(db: Session = Depends(get_db)):
    return db.query(_mod.Department).all()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

