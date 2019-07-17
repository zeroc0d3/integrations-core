#!/bin/bash
# Download istio
curl -L https://git.io/getLatestIstio | ISTIO_VERSION=$ISTIO_VERSION sh -
export PATH=$PWD/istio-$ISTIO_VERSION/bin:$PATH
echo "$CA_CERTIFICATE" > ca.crt

# Create kubectl context
kubectl config --kubeconfig=ci set-cluster k8s --server=$K8S_SERVER --certificate-authority=ca.crt
kubectl config --kubeconfig=ci set-credentials admin --username=$K8S_USERNAME --password=$K8S_PASSWORD
kubectl config --kubeconfig=ci set-context k8s-ci --cluster=k8s --namespace=default --user=admin
kubectl config --kubeconfig=ci use-context k8s-ci
export KUBECONFIG=ci

kubectl create serviceaccount --namespace kube-system tiller || true
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller || true
helm init --upgrade --service-account tiller --wait
kubectl create ns istio-system || true
kubectl label namespace default istio-injection=enabled

# istio-init install
helm install ./istio-$ISTIO_VERSION/install/kubernetes/helm/istio-init --name istio-init --namespace istio-system --set prometheus.enabled=true --version $ISTIO_VERSION --wait
kubectl wait jobs --all --for=condition=complete --namespace=istio-system --timeout=300s

# istio install
helm install ./istio-$ISTIO_VERSION/install/kubernetes/helm/istio --name istio --namespace istio-system --set prometheus.enabled=true --version $ISTIO_VERSION --wait

# Example application install
kubectl apply -f ./istio-$ISTIO_VERSION/samples/bookinfo/platform/kube/bookinfo.yaml
kubectl wait pods --all --for=condition=Ready --timeout=300s

# Adds a gateway to the app
kubectl apply -f ./istio-$ISTIO_VERSION/samples/bookinfo/networking/bookinfo-gateway.yaml
kubectl wait pods --all --for=condition=Ready --timeout=300s

# Make sure the application works, no log but fail if error.
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')

#curl -s http://$INGRESS_HOST:$INGRESS_PORT/productpage | grep -o "<title>.*</title>"

# Port forward citadel
# kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l istio=citadel -o jsonpath='{.items[0].metadata.name}') 16000:15014 &
# CITADEL_PID=$!

# Port forward mesh
# kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=telemetry -o jsonpath='{.items[0].metadata.name}') 16001:42422 &
# MESH_PID=$!

# Port forward telemetry
# kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l app=telemetry -o jsonpath='{.items[0].metadata.name}') 16002:15014 &
# MIXER_PID=$!

# Port forward galley
# kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l istio=galley -o jsonpath='{.items[0].metadata.name}') 16003:15014 &
# GALLEY_PID=$!

# Port forward pilot
# kubectl -n istio-system port-forward $(kubectl -n istio-system get pod -l istio=pilot -o jsonpath='{.items[0].metadata.name}') 16004:15014 &
# GALLEY_PID=$!
