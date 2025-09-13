# Step 1: Use an official Python image as base
FROM python:3.13.3

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy requirements first (better for caching)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the app (your code + model file)
COPY . .

# Step 6: Expose port 8000 (FastAPI default)
EXPOSE 8000

# Step 7: Command to run FastAPI app with Uvicorn
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
