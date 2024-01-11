from fastapi import FastAPI
from contextlib import asynccontextmanager
# from api.order.order_view import router as Order_router
from core.models import Base, db_helpr


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helpr.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI()
# app.include_router(Order_router)




 
