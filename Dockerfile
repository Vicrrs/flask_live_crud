# Base image
FROM python:3.11-slim-buster

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the Poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Disable the creation of virtual environments and install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the application code to the container
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the Flask application
CMD ["poetry", "run", "flask", "run"]
