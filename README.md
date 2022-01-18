## Simple in-memory cache API
---
This is simple in-memory exposed through API endpoints. 
Endpoints:
- GET /get/<key> - gets the value of the given key
- POST /set "{\"xyz-3\": \"xyz3\",\"abc-3\": \"abc3\"}" - sets the value of the new/existing keys
- GET /search?prefix=x&suffix=3 - filters the keys based on prefix and suffix, returns a list

### Building the application
```
## dsayan154 in the following lines needs to be replaced with some other accessible container registry
docker build -t dsayan154/imple-api:v0.1 . 
docker push dsayan154/simple-api:v0.1
```

### Deploy the k8s manifests
```
cd manifests
kubectl apply -f .
``` 
