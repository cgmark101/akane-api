from pydantic import BaseModel, HttpUrl, constr, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

class Info(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    title: constr(min_length=4, to_lower= True)
    synopsis: str
    rating: float
    anime_id: str
    key: str
    poster: str
    url: HttpUrl
    status: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
            }