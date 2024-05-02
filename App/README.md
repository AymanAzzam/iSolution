# Build/Test App Image
1. Build the image
```bash
docker build -t app:1.0 .
```
2. Run container from the image to test
```bash
docker run --name app -p 80:8080 -e DB_HOST="test" -e DB_PORT="8888" -e DB_USERNAME="test" -e DB_PASSWORD="test" app:1.0
```
3. Delete the container
```bash
docker rm $(docker stop $(docker ps -a --filter ancestor=app:1.0 -q ))
```
4. Push the image to docker hub
```bash
docker login
docker tag app:1.0 <docker-hub-username>/app:1.0
docker push <docker-hub-username>/app:1.0
```