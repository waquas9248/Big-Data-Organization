FROM almalinux:9.1
WORKDIR /app
COPY . /app
RUN  yum update -y \
&& yum upgrade -y \
&& yum install -y fuse \
&& yum install -y python3 \
&& cp gcsfuse.repo /etc/yum.repos.d/ \ 
&& yum install -y gcsfuse \
&& yum install -y python3-pip \
&& pip install scikit-learn \
&& pip install pandas \
&& pip install matplotlib \
&& pip install google-cloud-storage \
&& export GOOGLE_APPLICATION_CREDENTIALS=/app/se-413-375302-7cd244d5721a.json \
&& export PYTHONBUFFERED=1 \
&& mkdir /mnt/Google \
&& chmod 777 /mnt/Google
