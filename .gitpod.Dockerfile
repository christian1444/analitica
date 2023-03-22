FROM gitpod/workspace-base
RUN apt update
RUN apt install -y python3-pip
USER gitpod
RUN pip install pandas
