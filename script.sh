docker build -t week11/kubernetestodo:week11 .
#to push to docker hub
docker push week11/kubernetestodo:week11 
#to deploy the app to kubernetes
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
