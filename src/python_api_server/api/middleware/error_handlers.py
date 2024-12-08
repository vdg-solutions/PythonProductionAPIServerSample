from fastapi import Request
from python_api_server.core.logging import logger

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return {"error": "Internal server error"}, 500 