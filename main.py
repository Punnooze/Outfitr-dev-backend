from fastapi import FastAPI
from routes.auth_routes import auth_router 
from routes.user_route import user_router
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key ='OUTFITRR')
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(user_router)

