FROM centos:7.3.1611

# Java arguments
ARG java_jre_version=8u131
ARG java_jre_build_num=b11
ARG java_jre_download_hash=d54c1d3a095b4ff2b6607d096fa80163
ARG java_jre_checksum=ebebfd327e67c4bbe47dabe6b9f6e961
ARG java_home=/usr/java/latest

# envrionment variables
ENV JAVA_HOME ${java_home} 
ENV PATH $JAVA_HOME/bin:$PATH

# Java Installation
RUN yum install -y wget && \
  wget --quiet --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/${java_jre_version}-${java_jre_build_num}/${java_jre_download_hash}/jre-${java_jre_version}-linux-x64.rpm" && \
  echo "${java_jre_checksum}  jre-${java_jre_version}-linux-x64.rpm" >> MD5SUM && \
  md5sum -c MD5SUM && \
  yum install -y "jre-${java_jre_version}-linux-x64.rpm" \
  && yum clean all \
  && rm -rf "jre-${java_jre_version}-linux-x64.rpm" \
  && update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java 999999

ARG talend_job=${talend_job}
ARG talend_version=${talend_version}

ENV TALEND_JOB ${talend_job}
ENV TALEND_VERSION ${talend_version}
ENV ARGS ""

LABEL maintainer="marodeur100@talend.com" \
    talend.job=${talend_job} \
    talend.version=${talend_version}

WORKDIR /opt/talend

COPY talend/jobs/${TALEND_JOB}_${talend_version}.zip .

### Install Talend Job
RUN yum install -y unzip && \
    unzip ${TALEND_JOB}_${TALEND_VERSION}.zip && \
    rm -rf ${TALEND_JOB}_${TALEND_VERSION}.zip && \
    chmod +x ${TALEND_JOB}/${TALEND_JOB}_run.sh

# Copy the input files
COPY talend/input_files ./input_files 

CMD ["/bin/sh","-c","${TALEND_JOB}/${TALEND_JOB}_run.sh ${ARGS}"]
