.PHONY: build deploy_dag

build:
	docker build -t marodeur100/loadstatetostaging:0.1 --build-arg talend_job=LoadStateToStaging --build-arg talend_version=0.1 .
	docker build -t marodeur100/loadcustomerstostaging:0.1 --build-arg talend_job=LoadCustomersToStaging --build-arg talend_version=0.1 .
	docker build -t marodeur100/loadaggrcustomers:0.1 --build-arg talend_job=LoadAggrCustomers --build-arg talend_version=0.1 .
	docker build -t marodeur100/extractcustomernf:0.1 --build-arg talend_job=ExtractCustomerNF --build-arg talend_version=0.1 .

run_compose:
	docker-compose -f docker-compose-stg.yml up -d

stop_compose:
	docker-compose -f docker-compose-stg.yml down

deploy_dag:
	sed -i "s|/home/osboxes/out/|$$PWD/talend/output_file/|g" dags/talend_kubernetes_example.py
	sed -i "s|/home/osboxes/in/|$$PWD/talend/input_files/|g" dags/talend_kubernetes_example.py
	WEB="$(shell sudo kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | grep "airflow" | head -1)"; sudo kubectl cp dags/talend_kubernetes_example.py "$$WEB":/root/airflow/dags -c scheduler

clean_pods:
	sudo kubectl delete pods --field-selector status.phase!=Running
