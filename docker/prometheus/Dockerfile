FROM ubuntu:latest

## Step 1:
# Create a working directory
Workdir /etc/prometheus

## Step 2:
# Install prometheus
Run apt-get update
Run apt-get install wget apt-transport-https ca-certificates gnupg curl -y
Run wget https://github.com/prometheus/prometheus/releases/download/v2.51.2/prometheus-2.51.2.linux-amd64.tar.gz
Run tar xf prometheus-2.51.2.linux-amd64.tar.gz --strip-components=1

## Step 3:
# Install gcloud
Run curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
Run echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
Run apt-get update && apt-get install google-cloud-cli -y
Run apt-get install google-cloud-cli-gke-gcloud-auth-plugin -y

## Step 4:
# Install kubelet
Run curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
Run apt-get install kubectl -y

## Step 5:
# Configure prometheus
COPY ./scripts/prometheus.yaml /etc/prometheus/prometheus.yml
COPY ./scripts/config /etc/prometheus/config

## Step 6:
# Expose port 9090
EXPOSE 9090
