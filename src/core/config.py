from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:/// ./db_sqlite3_shop"


settings = Settings()