.PHONY: run build

build:
	docker build -t marodeur100/loadstatetostaging:0.1 --build-arg talend_job=LoadStateToStaging --build-arg talend_version=0.1 .
	docker build -t marodeur100/loadcustomerstostaging:0.1 --build-arg talend_job=LoadCustomersToStaging --build-arg talend_version=0.1 .
	docker build -t marodeur100/loadaggrcustomers:0.1 --build-arg talend_job=LoadAggrCustomers --build-arg talend_version=0.1 .
	docker build -t marodeur100/extractcustomernf:0.1 --build-arg talend_job=ExtractCustomerNF --build-arg talend_version=0.1 .



