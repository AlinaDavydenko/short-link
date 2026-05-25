from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import UrlCreate, UrlResponse
from app.utils import generate_short_code
from sqlalchemy.orm import Session
from app.db_core.session import get_session
from app.db_core.models import Url

router = APIRouter()


@router.post("/shorten", response_model=UrlResponse)
def shorten_url(url: UrlCreate, session=Depends(get_session)):
    # 1 получи original_url из url.original_url
    original_url = str(url.original_url)

    existing_url = session.query(Url).filter(Url.original_url == original_url).first()
    if existing_url:
        return existing_url

    # 2 сгенерируй short_code через generate_short_code()
    short_code = generate_short_code()

    new_url = Url(original_url=original_url, short_code=short_code, clicks=0)

    session.add(new_url)
    session.commit()
    session.refresh(new_url)

    # 3 верни UrlResponse
    return new_url


@router.get("/{short_code}")
def redirect_url(short_code: str, session=Depends(get_session)):
    # 1 Найди в базе по short_code
    url = session.query(Url).filter(Url.short_code == short_code).first()

    # 2 Если не нашла — ошибка 404
    if not url:
        raise HTTPException(status_code=404, detail="Url not found")

    # 3 Увеличь clicks на 1
    url.clicks += 1
    session.commit()

    # 4 Сделай редирект
    return RedirectResponse(url=url.original_url)
