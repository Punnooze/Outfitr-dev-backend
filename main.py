from fastapi import FastAPI
from routes.user_route import user_router
from routes.product_routes import product_router
from routes.misc_routes import misc_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key ='OUTFITRR')

app.include_router(user_router)
app.include_router(product_router)
app.include_router(misc_router)

