from fastapi import FastAPI
from app.router import router
from app.db_core.database import init_db

# 1 Создать FastAPI приложение
app = FastAPI()

# 2 Подключить роутер
app.include_router(router)

# 3 При старте создать таблицы в базе
init_db()
