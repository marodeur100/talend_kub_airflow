# Streaming Example

## Prerequists
* Run [Talend, Kubernetes & Airflow demo](https://github.com/marodeur100/talend_kub_airflow)

## Deploy Pods
* Execute ```sudo make run```
* Check if everything is running with ```sudo make get_pods```

## Start CDC
* Execute ```make cdc```

## View results in elasticsearch
* Install elastic head plugin in firefox
* connect elastic head to localhost:30192
* Index customer_nf should be visible 
