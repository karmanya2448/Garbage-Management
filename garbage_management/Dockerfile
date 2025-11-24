# Use Python
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy only dependency file first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy rest of the project
COPY . .

# Run your app
CMD ["python", "app.py"]
