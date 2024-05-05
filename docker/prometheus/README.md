# Build Prometheus Image
1. Build the image
```bash
docker build -t prometheus:1.0 .
```
2. Run container from the image to test
```bash
docker run --name prometheus -p 9090:9090 prometheus:1.0
```
3. Delete the container
```bash
docker rm $(docker stop $(docker ps -a --filter ancestor=prometheus:1.0 -q ))
```
4. Push the image to docker hub
```bash
docker login
docker tag prometheus:1.0 <docker-hub-username>/prometheus:1.0
docker push <docker-hub-username>/prometheus:1.0
```