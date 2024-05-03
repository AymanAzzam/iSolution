# Helm Chart of App deployment
1. Install the app helm chart
```bash
helm install --set imageTag="1.0" app  ./app/
```
2. Deploy version 2 of the app
```bash
helm upgrade --set imageTag="2.0" app  ./app/
```