FROM mysql:latest 
 
## Step 1:
# Create a working directory
Workdir /database

# ## Step 2:
# # Install Vault CLI
Run microdnf install yum
Run yum install -y yum-utils
Run yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
Run yum -y install vault
Run yum -y reinstall vault

## Step 3:
# Copy scrupts to working directory
COPY . /database

## Step 4:
# Expose port 3306
Expose 3306 