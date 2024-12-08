from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from python_api_server.core.logging import logger
from python_api_server.core.config import settings
from python_api_server.api.routes import health_router
from python_api_server.api.middleware.error_handlers import global_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up API server...")
    yield
    logger.info("Shutting down API server...")

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description="Production-ready API server",
        version="1.0.0",
        lifespan=lifespan
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=settings.CORS_HEADERS,
    )

    # Include routers
    app.include_router(health_router, prefix=settings.API_V1_PREFIX)
    
    # Add exception handler
    app.exception_handler(Exception)(global_exception_handler)

    return app

app = create_app()