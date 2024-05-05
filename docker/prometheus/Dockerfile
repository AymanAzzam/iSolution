FROM prom/prometheus

## Step 1:
# Copy configuration to nginx directory
COPY ./scripts/prometheus.yaml /etc/prometheus/prometheus.yml

## Step 2:
# Expose port 80
EXPOSE 9090