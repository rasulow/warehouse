from fastapi import FastAPI, Request, Response, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core import Base, engine, SessionLocal, auth_router
import routers

app = FastAPI(
    swagger_ui_parameters={
        "syntaxHighlight": False
    },
    title='Warehouse'
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


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

app.mount('/uploads', StaticFiles(directory="uploads"), name="uploads")
Base.metadata.create_all(engine)

app.include_router(auth_router)
app.include_router(routers.department_router)
app.include_router(routers.position_router)
app.include_router(routers.user_router)
app.include_router(routers.category_router)
app.include_router(routers.item_router)
app.include_router(routers.image_router)
app.include_router(routers.request_router)
app.include_router(routers.response_router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=5050, reload=True)
