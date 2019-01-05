
#Master DevOps Data Architectures with Apache Airflow, Kubernetes and Talend
The Demo will run 4 Talend ETL jobs on Airflow/Minikube using the new KuberntesPodOperator. Two CSV input files with customers and states will be aggregated into a postgres DB and finally written out into a CSV result file.

Follow the guide step by step
# Ubuntu Image Installation on Windows 10
* Download and install [Virtual Box](https://www.virtualbox.org/)
* Download Ubuntu 18.04 64Bit VDI [Image](https://www.osboxes.org/)
* Create New Linux Ubuntu 64 Bit VM in your VirtualBox and use VDI Image as Filesystem
* Assigne 10GB RAM and 4 CPU minimum 
* Start VM and open a console
* Correct keyboard layout: sudo dpkg-reconfigure keyboard-configuration

# Docker 18.06 Install
```shell
# Curl
sudo apt-get install curl
# Docker 18.06
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt-get install docker-ce=18.06.1~ce~3-0~ubuntu
# Docker permissions
sudo usermod -aG docker ${USER}
su - ${USER}
# Docker-Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

# Minikube 28.02 and Kubectl
* Follow the steps of the [Installation Guide](https://computingforgeeks.com/how-to-install-minikube-on-ubuntu-18-04/)
* Attention: Install Minikube 28.02, latest did not work properly when I tried it
```shell
curl -SLO https://github.com/kubernetes/minikube/releases/download/v0.28.2/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube
```

# (Re)Start steps for Minikube
```shell
cd /etc/kubernetes/ && \
sudo rm *.conf && \
cd && \
sudo minikube delete # may also need rm -rf ~/.minikube && \
sudo minikube start --vm-driver=none
sudo minikube status
```

# Install Airflow on Kubernetes
* in your home directory:
```shell
git clone https://github.com/apache/airflow
# Build
export SLUGIFY_USES_TEXT_UNIDECODE=yes
./scripts/ci/kubernetes/Docker/build.sh
# Deploy
sudo ./scripts/ci/kubernetes/kube/deploy.sh -d persistent_mode
```
* Wait until airflow comes up (may take 2 minutes)
* You should be able to connect to the Airflow UI via http://localhost:30809 
* Login with airflow/airflow

# Install the example
* in your home directory:
```shell
git clone https://github.com/marodeur100/talend_kub_airflow.git
# Build
sudo make build
# Deploy DAG to airflow
sudo make deploy_dag
```

# Start the Example
* in the airflow UI: enable and start talend_kubernetes_example
* check pods created, running and completed with:
```shell
sudo kubectl get pods
```
* Find input CSVs under talend/input_files
* Find result CSV under talend/output_file
