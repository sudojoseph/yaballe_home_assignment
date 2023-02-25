from pydantic import BaseModel, validator
from .global_schema_validators import has_min_length, validate_source


class ProductSchema(BaseModel):
    product_id: str
    title: str
    price: float or int
    source: str

    
    @validator('product_id')
    def product_id_length(cls, value):
        has_min_length('product id', value, 3)
    

    @validator('title')
    def title_length(cls, value):
        has_min_length('title', value, 2)
    

    @validator('price')
    def price_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('price must be positive')
        return value
    

    @validator('source')
    def source_value(cls, value):
        validate_source(value)
        has_min_length('source', value, 1)
        
    

