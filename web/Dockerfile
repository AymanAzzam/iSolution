FROM nginx:latest

## Step 1:
# Copy configuration to nginx directory
COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template

## Step 2:
# Expose port 80
EXPOSE 80

## Step 3:
# Run nginx
CMD ["nginx", "-g", "daemon off;"]