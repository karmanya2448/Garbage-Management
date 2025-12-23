# Use Python

FROM python:3.12-slim


# Set working directory
WORKDIR /app

# Copy only dependency file first
COPY requirements.txt .


# Install dependencies, excluding pywin32 which is Windows-specific
RUN grep -v "pywin32" requirements.txt > requirements_linux.txt && \
    pip install -r requirements_linux.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy rest of the project
COPY . .


# Expose the port
EXPOSE 8000

# Run your app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



