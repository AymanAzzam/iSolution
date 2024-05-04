From python:3.10

## Step 1:
# Create a working directory
Workdir /app

## Step 2:
# Install Vault CLI
Run apt-get update && apt-get install -y lsb-release 
Run wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
Run echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list
Run apt-get update && apt-get install -y vault

## Step 3:
# Copy source code to working directory
Copy . /app

## Step 4:
# Install packages from requirements.txt
Run pip install -r requirements.txt

## Step 5:
# Expose port 80
Expose 80

## Step 6:
# Run app.py at container launch
Cmd [ "flask","run","--host=0.0.0.0", "--port=8080" ]