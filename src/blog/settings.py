from pydantic import BaseSettings
from os import environ


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url: str = "postgresql://postgres:1234@localhost/blog"
    jwt_secret: str = "jEGoJf7NN69Q3SaAWkicrgwlTQXbOg3X1c7yoitp-F4"
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
