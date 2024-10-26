from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Tables cleared')
    await create_tables()
    print('Tables created')
    yield
    print('Shutdown')

app = FastAPI(lifespan=lifespan)
app.include_router(router)
