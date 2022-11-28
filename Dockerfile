FROM ubuntu:20.04
COPY . /app/

RUN apt-get update 
# Install gcloud

# Install git
RUN apt-get install -y git
# Install Python
RUN apt-get install --no-install-recommends -y python3.8 python3-pip 
# Install dbt
RUN python3 -m pip install -r /app/requirements.txt
