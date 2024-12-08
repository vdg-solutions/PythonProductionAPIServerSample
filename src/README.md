# Python API Server

A production-ready FastAPI server with a clean architecture.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `python_api_server/.env.example` to `python_api_server/.env` and adjust values
6. Run the server: `python run.py`

## API Endpoints

- `GET /api/v1/health` - Health check endpoint
  - Response: `{"status": "healthy"}`

## Environment Variables

Configuration is handled through environment variables. Copy `.env.example` and adjust as needed:

- `APP_NAME` - Name of the application
- `DEBUG` - Debug mode (True/False)
- `API_V1_PREFIX` - API version prefix
- `DATABASE_URL` - Database connection string
- `SECRET_KEY` - Secret key for security
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time

## Project Structure 
./
├── README.md           # Project documentation
├── requirements.txt    # Project dependencies
├── run.py             # Server startup script
└── python_api_server/  # Main package directory
    ├── api/           # API-related code
    │   ├── routes/    # API endpoints
    │   └── middleware/# Custom middleware
    └── core/          # Core functionality
        ├── config.py  # Application configuration
        └── logging.py # Logging setup

## Development

### Running Tests