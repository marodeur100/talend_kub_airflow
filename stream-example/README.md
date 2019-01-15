# Streaming Example

## Prerequists
* Run [Talend, Kubernetes & Airflow demo](https://github.com/marodeur100/talend_kub_airflow)

## Deploy Pods
* Execute ```sudo make run```
* Check if everything is running with ```sudo make get_pods```

## Start CDC
* Execute ```make cdc```

## Start Streamdata Generator
* The generator sends dummy test data to the topic test
```shell
sudo apt-get install python-pip
pip install kafa
python stream/kafka_producer.py localhost:30092 test
```
