from pydantic_settings import BaseSettings
from typing import List, Union

class Settings(BaseSettings):
    """
    Application settings and configuration.
    
    Loads settings from environment variables and .env file.
    Environment variables take precedence over .env file values.
    """
    
    # Application settings
    APP_NAME: str = "Production API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    WORKERS_COUNT: int = 4
    
    # CORS settings
    CORS_ORIGINS: Union[List[str], List[Pattern]] = ["*"]  # In production, replace with actual domains
    CORS_HEADERS: List[str] = ["*"]
    CORS_METHODS: List[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
    ALLOW_CREDENTIALS: bool = True
    
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/db"
    DB_MAX_CONNECTIONS: int = 10
    DB_TIMEOUT: int = 30
    
    # Security settings
    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # API Documentation settings
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"
    
    # Logging settings
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        """Pydantic model config"""
        env_file = ".env"
        case_sensitive = True
        
        # You can add additional config here
        validate_assignment = True
        extra = "forbid"

    @property
    def fastapi_kwargs(self) -> dict:
        """
        FastAPI configuration arguments.
        Used in the FastAPI app initialization.
        """
        return {
            "debug": self.DEBUG,
            "title": self.APP_NAME,
            "version": self.VERSION,
            "docs_url": self.DOCS_URL if self.DEBUG else None,
            "redoc_url": self.REDOC_URL if self.DEBUG else None,
            "openapi_url": self.OPENAPI_URL if self.DEBUG else None,
        }
    
    @property
    def cors_kwargs(self) -> dict:
        """
        CORS configuration arguments.
        Used in the CORS middleware.
        """
        return {
            "allow_origins": self.CORS_ORIGINS,
            "allow_methods": self.CORS_METHODS,
            "allow_headers": self.CORS_HEADERS,
            "allow_credentials": self.ALLOW_CREDENTIALS,
        }

# Create settings instance
settings = Settings()

# Don't allow further modification of settings
# settings.__config__.frozen = True 