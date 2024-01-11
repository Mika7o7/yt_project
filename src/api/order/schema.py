from pydantic import BaseModel


class Order(BaseModel):
    outside_number: int 
    title: str 
    description: str | None = None
    type: str
    gem: str | None = None
    metal: str | None = None
    

