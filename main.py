from fastapi import FastAPI
from routes.user_route import user_router
from starlette.requests import Request

from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key ='OUTFITRR')
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_router)

