
build:
	sudo docker build \
    --build-arg SPARK_VERSION_KEY=spark-1.6.3-bin-hadoop2.6 \
    -t spark-2.1.0-bin-hadoop2.6 .

run:
	sudo kubectl apply -f spark.yaml

get_pods:
	sudo kubectl get pods -n stream

generate:
	python kafka_producer.py localhost:30092 test

