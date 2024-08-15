from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    url: HttpUrl

class URLCreate(URLBase):
    pass

class URL(URLBase):
    short_code: str

    class Config:
        from_attributes = True # Changed from orm_mode = True