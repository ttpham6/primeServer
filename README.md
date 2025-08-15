# primeServer
Repository for the REST JSON API portion of the primeServer
A full deployment includes downloading this source from: 
https://github.com/ttpham6/primeServer

The complementary client code is located in:
https://github.com/ttpham6/primeClient



# Configure and Deploy
<p> These directions outline deploying the code and image using minikube and kubectl
</p>

* Start minikube if it has not already been started
    - minikube status
    - minikube start --driver=docker
* Cleanup is required if this is a reinstall
    - kubectl get all
    - kubectl delete deployment api-server-deploy 
    - kubectl delete service api-service
    - kubectl get all
    - kubectl delete pod prime-api
* Installation
    - Set the environment variable to build image and save it directly to minikube
        - eval $(minikube docker-env)
    - Build image from current Dockerfile
        - minikube image build -t prime-api:latest .
    - Deploy the pod 
        - kubectl apply -f deploy.yaml
    - Deploy the service  
        - kubectl apply -f api-service.yaml 
    - Unset the environment
        - eval $(minikube docker-env -u)

# Succesful Deployment
* Start the browser and api
    - minikube service api-service

# Troubleshooting Commands
* kubectl get all
* minikube ip
* kubectl get pods --all-namespaces
* kubectl get deployments
* kubectl exec -it container_ID_or_name -- sh
* Docker image commands
    - docker image list
    - docker pull <image-name>
        - For example: python:3.13.6-slim-bookworm>
    - docker rmi <image_id>

