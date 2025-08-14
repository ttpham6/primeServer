# primeServer
Repository for API to calculate primes

# Configure and Deploy
<p> These directions outline deploying the code and image using minikube and kubectl
</p>


* Start minikube if it has not already been started 
    - minikube start
* Set the environment variable to make changes directly to minikube
    - eval $(minikube docker-env)
* Build image
    - minikube image build -t prime-api:latest .
* Unset the environment
    - eval $(minikube docker-env -u)
* Activate changes 
    - kubectl apply -f prime-api-deployment.yaml 

# Verifying that deplyoment was susccesful

* Start the browser and api
    - minikube service prime-api-service

# Useful troubleshooting commands

* minikube ip
* kubectl get pods --all-namespaces
* kubectl get deployments