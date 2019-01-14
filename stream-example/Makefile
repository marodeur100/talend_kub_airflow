
run:
	sudo kubectl create -f stream.yaml

delete:
	sudo kubectl delete namespace stream

get_pods:
	sudo kubectl get pods --namespace=stream

cdc:
	curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:30083/connectors/ -d @es-sink.json
	curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:30083/connectors/ -d @register-postgres.json

logs:
	POD_NAME="$(shell sudo kubectl get pods -l "app=debezium-connect-source" -o jsonpath="{.items[0].metadata.name}" --namespace=stream)"; sudo kubectl logs $$POD_NAME --namespace=stream
 
