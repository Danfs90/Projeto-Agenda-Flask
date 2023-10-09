from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import DeclarativeBase,Mapped
from sqlalchemy import Integer,DateTime,VARCHAR,String, Column, ForeignKey
from sqlalchemy.orm import mapped_column,relationship


class Base(DeclarativeBase):
    pass



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    DATABASE_URL: str
