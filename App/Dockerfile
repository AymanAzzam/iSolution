From python:3.10

## Step 1:
# Create a working directory
Workdir /app

## Step 2:
# Copy source code to working directory
Copy . /app

## Step 3:
# Update linux packages
Run apt-get update

## Step 4:
# Install packages from requirements.txt
Run pip install -r requirements.txt

## Step 5:
# Expose port 80
Expose 80

## Step 6:
# Run app.py at container launch
Cmd [ "flask","run","--host=0.0.0.0", "--port=8080" ]