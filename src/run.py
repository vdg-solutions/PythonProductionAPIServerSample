import uvicorn
from python_api_server.core.config import settings
from python_api_server.core.logging import logger

if __name__ == "__main__":
    logger.info(f"Starting {settings.APP_NAME} in {'debug' if settings.DEBUG else 'production'} mode")
    uvicorn.run(
        "python_api_server.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        workers=4,
        log_level="debug" if settings.DEBUG else "info",
        reload=settings.DEBUG
    )
