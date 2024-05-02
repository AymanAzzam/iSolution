# Build Mysql Image
1. Build the image
```bash
docker build -t mysql:1.0 .
```
2. Run container from the image to test
```bash
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD="test@2024" mysql:1.0
```
3. Delete the container
```bash
docker rm $(docker stop $(docker ps -a --filter ancestor=mysql:1.0 -q ))
```
4. Push the image to docker hub
```bash
docker login
docker tag mysql:1.0 <docker-hub-username>/mysql:1.0
docker push <docker-hub-username>/mysql:1.0
```