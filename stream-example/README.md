# Streaming Example

## Prerequists
* Run [Talend, Kubernetes & Airflow demo](https://github.com/marodeur100/talend_kub_airflow)

## Deploy Pods
* Execute ```sudo make run```
* Check if everything is running with ```sudo make get_pods```

## Start CDC
* Execute ```make cdc```

## Setup pyspark and jupyther
* Install Spark
```shell
cd /opt && \
    curl http://www.us.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.6.tgz | \
        sudo tar -zx && \
    sudo ln -s spark-2.4.0-bin-hadoop2.6 spark && \
    echo Spark 2.4.0 installed in /opt
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```
* Install jupyter 
```
sudo apt-get install python-pip
pip install jupyter
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```
* Start a notebook with ```pyspark```

## Start Streamdata Generator
* The generator sends dummy test data to the topic test
```shell
pip install kafa
python stream/kafka_producer.py localhost:30092 test
```
