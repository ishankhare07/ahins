create_ingress_gcp:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/cloud/deploy.yaml
	# wait for ingress controller
	sleep 5
	# kubectl wait --for=condition=Running --timeout=2m pods -n ingress-nginx -l app.kubernetes.io/component=controller

remove_ingress_gcp:
	kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/cloud/deploy.yaml

remove_ingress_resources:
	kubectl delete -f ./kube/deploy.yaml
	# next expose it with an ingress rule
	kubectl delete -f ./kube/ingress.yaml


create_echo_service_with_ingress_rule:
	# first create the deployment and service
	kubectl apply -f ./kube/deploy.yaml
	# next expose it with an ingress rule
	kubectl apply -f ./kube/ingress.yaml

nginx_controller_pod = $(shell kubectl get pods -n ingress-nginx --no-headers | grep 'nginx-controller' | cut -d' ' -f1)

test_ingress_service:
	kubectl exec -it -n ingress-nginx $(nginx_controller_pod) -- curl http-echo-service.default.svc.cluster.local:5678

clean: remove_ingress_gcp remove_ingress_resources
