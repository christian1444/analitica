FROM gitpod/workspace-base
RUN apt update
RUN apt install -Y python3-pip
USER gitpod
