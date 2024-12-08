To run the server:
1. Without Docker:
    - Install dependencies: `pip install -r requirements.txt`
    - Run the server: `python -m src.run`

2. With Docker:
    - Build the image: `docker build -t api-server .`
    - Run the container: `docker run -p 8000:8000 api-server`

