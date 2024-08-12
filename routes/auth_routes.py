from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse, JSONResponse
from config.config import CLIENT_ID, CLIENT_SECRET
from authlib.integrations.starlette_client import OAuth, OAuthError


oauth = OAuth()
oauth.register(
    name = 'google',
    server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    client_kwargs = 
    {
        'scope': 'openid email profile',
        'redirect_url': 'http://localhost:8000//auth'
    }
)


auth_router = APIRouter()
templates = Jinja2Templates(directory="templates")

@auth_router.get("/")
def read_root(request: Request):
    user = request.session.get('user')
    if user:
        return RedirectResponse('/welcome')
    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
    )

@auth_router.get("/welcome")
def welcome(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse('/')
    return  JSONResponse({'message': 'Welcome!', 'user': user.get('name')})

@auth_router.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)

@auth_router.get("/auth")
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse('/welcome')

@auth_router.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('/')

# from fastapi import APIRouter, HTTPException
# from fastapi.templating import Jinja2Templates
# from starlette.requests import Request
# from starlette.responses import RedirectResponse
# from config.config import CLIENT_ID, CLIENT_SECRET
# from authlib.integrations.starlette_client import OAuth, OAuthError


# oauth = OAuth()
# oauth.register(
#     name = 'google',
#     server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
#     client_id = CLIENT_ID,
#     client_secret = CLIENT_SECRET,
#     client_kwargs = 
#     {
#         'scope': 'openid email profile',
#         'redirect_url': 'http://localhost:8000//auth'
#     }
# )


# auth_router = APIRouter()
# templates = Jinja2Templates(directory="templates")

# @auth_router.get("/")
# def read_root(request: Request):
#     user = request.session.get('user')
#     if user:
#         return RedirectResponse('/welcome')
#     return templates.TemplateResponse(
#         name="home.html",
#         context={"request": request}
#     )

# @auth_router.get("/welcome")
# def welcome(request: Request):
#     user = request.session.get('user')
#     if not user:
#         return RedirectResponse('/')
#     return templates.TemplateResponse(
#         name='welcome.html',
#         context={'request': request, 'user': user}
#     )

# @auth_router.get("/login")
# async def login(request: Request):
#     url = request.url_for('auth')
#     return await oauth.google.authorize_redirect(request, url)

# @auth_router.get("/auth")
# async def auth(request: Request):
#     try:
#         token = await oauth.google.authorize_access_token(request)
#     except OAuthError as e:
#         return templates.TemplateResponse(
#             name='error.html',
#             context={'request': request, 'error': e.error}
#         )
#     user = token.get('userinfo')
#     if user:
#         request.session['user'] = dict(user)
#     return RedirectResponse('/welcome')

# @auth_router.get('/logout')
# def logout(request: Request):
#     request.session.pop('user')
#     request.session.clear()
#     return RedirectResponse('/')