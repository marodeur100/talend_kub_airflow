FROM java:openjdk-8-jdk


ENV spark_ver 2.4.0
ENV SCALA_VERSION 2.11

# Get Spark from US Apache mirror.
RUN mkdir -p /opt && \
    cd /opt && \
    curl http://www.us.apache.org/dist/spark/spark-${spark_ver}/spark-${spark_ver}-bin-hadoop2.6.tgz | \
        tar -zx && \
    ln -s spark-${spark_ver}-bin-hadoop2.6 spark && \
    echo Spark ${spark_ver} installed in /opt

# Spark Kafka Streaming
RUN cd /tmp && \
    wget http://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_${SCALA_VERSION}/${spark_ver}/spark-streaming-kafka-0-8-assembly_${SCALA_VERSION}-${spark_ver}.jar && \
    mv spark-streaming-kafka-0-8-assembly_${SCALA_VERSION}-${spark_ver}.jar /opt/spark/jars

ADD start-common.sh start-worker.sh start-master.sh /
RUN chmod +x /start-common.sh /start-master.sh /start-worker.sh
ENV PATH $PATH:/opt/spark/bin

