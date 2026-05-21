from pydantic import BaseModel, HttpUrl


class UrlCreate(BaseModel):
    original_url: HttpUrl


class UrlResponse(BaseModel):
    original_url: str
    short_code: str
    clicks: int
