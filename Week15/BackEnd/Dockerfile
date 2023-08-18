FROM python:3.8-slim
WORKDIR /app

# Install flask_cors
RUN pip install Flask-Cors

# Copy the backend files
COPY backend_app.py .

CMD ["python", "backend_app.py"]

