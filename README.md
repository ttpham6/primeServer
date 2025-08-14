# primeClient
Repository for the webUI portion of the primeServer


# Configure and Deploy
<p> These directions outline deploying the code and image using minikube and kubectl
</p>

* Start minikube if it has not already been started.
    - minikube status
    - minikube start --driver=docker
* Build image from current Dockerfile
    - minikube image build -t prime-api:latest .
* Deploy  
    - kubectl apply -f prime-api-deployment.yaml 

# Verifying that deplyoment was susccesful
* Start the browser and api
    - minikube service prime-api-service

# Useful troubleshooting commands
* minikube ip
* kubectl get pods --all-namespaces
* kubectl get deployments
* kubectl exec -it container_ID_or_name -- sh

* Docker image commands
    - docker image list
    - docker pull <python:3.13.6-slim-bookworm>
    - docker rmi <image_id>