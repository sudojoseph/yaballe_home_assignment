from pydantic import BaseModel, validator
from .global_schema_validators import has_min_length, validate_source


class UserSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    favorite_products: list = []

    
    @validator('first_name')
    def first_name_length(cls, value):
        has_min_length('first name', value, 2)
    

    @validator('last_name')
    def last_name_length(cls, value):
        has_min_length('last name', value, 2)
    

    @validator('email')
    def email_must_contain_at_symbol(cls, value):
        if '@' not in value:
            raise ValueError('email must contain @ symbol')
        return value
    

class UserFavoriteProductSchema(BaseModel):
    product_id: str
    source: str

    
    @validator('product_id')
    def product_id_length(cls, value):
        has_min_length('product id', value, 3)
    

    @validator('source')
    def sourse_length(cls, value):
        has_min_length('source', value, 2)
        validate_source(value)