#!bin/bash
kubectl 'action' 'resource'

minikube start

kubectl get po -A  -> access new cluster
minikube kubectl -- get po -A -> download appropriate versioin of kubectl
minikube dashboard
minikube pause
minikube unpause
minikube stop
minikube config set memory 9001 (requires restart)
minikube addons list
minikube start -p aged --kubernetes-version=v1.16.1
minikube delete --all

kubectl create deployment 
kubectl get deployments (lists all deployments)
kubectl proxy (create proxy that will forward communications cluster wide)

kubectl get - list resources
kubectl describe - show detailed information about a resource
kubectl logs - print the logs from a container in a pod
kubectl exec - execute a command on a container in a pod

kubectl get pods
kubectl describe pods  

export POD_NAME="$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')"
echo Name of the Pod: $POD_NAME (query pod name directly throught proxy and store it)

curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/ (to see output)
kubectl logs "$POD_NAME" (container logs)
kubectl exec "$POD_NAME" -- env (execute commands on the pod when up and running)
kubectl exec -ti $POD_NAME -- bash (start a bash session)
cat server.js (source code)
curl http://localhost:8000 (check to see app up and running)

------------ Port Forward ------------
kubectl port-forward [resource-type]/[resource-name] [local-port]:[resource-port]

    [resource-type]: The type of Kubernetes resource (e.g., pod, svc).
    [resource-name]: The name of the Kubernetes resource.
    [local-port]: The local port on your machine.
    [resource-port]: The port on the Kubernetes resource.

kubectl -n [namespace] get svc
kubectl apply -f sample_service.yml

helm install airflow apache-airflow/airflow \
  --set executor=KubernetesExecutor \
  --create-namespace --namespace airflow
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow

