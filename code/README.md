# deployment

----
**credentials secret**

fill the `deployment/django/.dockerconfigjson` file with your own private registry credentials
The general format of this file is :
```yaml
{
    "auths": {
        "https://registry.gitlab.com":{
            "username":"REGISTRY_USERNAME",
            "password":"REGISTRY_PASSWORD",
            "email":"REGISTRY_EMAIL",
            "auth":"BASE_64_BASIC_AUTH_CREDENTIALS (see below)"
    	}
    }
}
```
The base 64 basic credentials mentioned above are the username and password in basic credentials format `{username}:{password}` , encoded with base64 format.

To achieve this simply run :
```bash
echo -n "{REGISTRY_USERNAME}:{REGISTRY_PASSWORD}" | base64
```

Create a file with above mentioned json format, and then base64 encode it for the Kubernetes secret.
```bash
cat .dockerconfigjson | base64
```

Create a file called `registry-credentials.yml` and add the following content

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
  namespace: default
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: BASE_64_ENCODED_DOCKER_FILE
```


Now we can create the secret in our cluster.
```bash
kubectl apply -f registry-credentials.yml
```

Specifying on a deployment
```yaml
imagePullSecrets: 
    - name: registry-credentials
```
---
**services**

for PostgreSQL database
```bash
kubectl create -f deployment/db/
```
for Django instance
```bash
kubectl create -f deployment/django/service.yaml
kubectl create -f deployment/django/route.yaml
kubectl create -f deployment/django/migration.yaml
```
if migration successfully done, you cab delete job, after all ...
```bash
kubectl create -f deployment/django/deployment.yaml
```

for auto scale
```bash
kubectl autoscale deploy django --max 10 --min=1 --cpu-percent=50
```

