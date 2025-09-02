from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TABNEWS_BASE_URL: str = "https://www.tabnews.com.br/api/v1"
    LLM_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USER: str
    SMTP_PASS: str
    FROM_EMAIL: str
    BATCH_SIZE: int = 500
    ENV: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()
