# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):

#     app_name: str = "AI Customer Agent"

#     environment: str = "development"

#     database_url: str

#     #openai_api_key: str
#     nvidia_api_key: str

#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )


# settings = Settings()
#  the following codes are for adding security to the project
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):

    app_name: str

    environment: str

    database_url: str

    openai_api_key: str

    secret_key: str

    jwt_algorithm: str = "HS256"

    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()