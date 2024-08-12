from fastapi import FastAPI
from routes.user_route import user_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key ='OUTFITRR')

app.include_router(user_router)

