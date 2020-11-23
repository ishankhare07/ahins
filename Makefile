create_ingress_gcp:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/cloud/deploy.yaml
	# wait for ingress controller

patch_ingress_service:
	kubectl wait --for=condition=Ready --timeout=2m pods -n ingress-nginx -l app.kubernetes.io/component=controller
	kubectl patch svc ingress-nginx-controller -n ingress-nginx -p '{"spec": {"loadBalancerIP": "${STATIC_IP}"}}'

remove_ingress_gcp:
	kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/cloud/deploy.yaml

remove_echo_service_ingress:
	kubectl delete -f ./test_infra/deploy.yaml
	# next expose it with an ingress rule
	kubectl delete -f ./test_infra/ingress.yaml

install_cert_manager:
	kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v0.15.1/cert-manager.yaml
	
create_echo_service_with_ingress_rule:
	# first create the deployment and service
	kubectl apply -f ./test_infra/deploy.yaml
	# next expose it with an ingress rule
	kubectl apply -f ./test_infra/ingress.yaml

nginx_controller_pod = $(shell kubectl get pods -n ingress-nginx --no-headers | grep 'nginx-controller' | cut -d' ' -f1)

install_prometheus:
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitor
remove_prometheus:
	helm uninstall prometheus --namespace monitor

test_ingress_service:
	kubectl exec -it -n ingress-nginx $(nginx_controller_pod) -- curl http-echo-service.default.svc.cluster.local:5678

clean: remove_ingress_gcp remove_echo_service_ingress
