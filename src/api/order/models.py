from sqlalchemy import Boolean, Column, Integer, String
 
from api.database import Base
 
class Todo(Base):
    __tablename__ = "todos"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)



class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    outside_number = Column(Integer, unique=True, index=True)
    title = Column(String)
    description = Column(String)
    type = Column(String)# надо чтобы можно было вибирать
    gem = Column(String)# надо чтобы можно было вибирать
    metal = Column(String)# надо чтобы можно было вибирать
    curent_section = Column(String)
