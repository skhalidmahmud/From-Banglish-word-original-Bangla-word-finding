# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
# We use app:app because app.py contains the FastAPI instance named 'app'
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
