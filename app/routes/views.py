from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.apis.api_a.mainmod import main_func as main_func_a
from app.apis.api_b.mainmod import main_func as main_func_b
from app.core.auth import get_current_user

router = APIRouter()

# Templates Jinja
templates = Jinja2Templates(directory="app/templates")


# include_in_schema=False Rota Oculta
@router.get("/", tags=["HTML"], response_class=HTMLResponse, include_in_schema=False)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_a(num)


@router.get("/api_b/{num}", tags=["api_b"])
async def view_b(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> dict[str, int]:
    return main_func_b(num)
