from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse

from app.core import auth
from app.routes import views

app = FastAPI(
    title="FastAPI Nano",
    description="Projeto Base",
    version="1.0.1",
    default_response_class=ORJSONResponse,
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(auth.router)
app.include_router(views.router)
