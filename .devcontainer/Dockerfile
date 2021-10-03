FROM python:3.9-buster

ARG USERNAME=python
# On Linux, replace with your actual UID, GID if not the default 1000
ARG USER_UID=1000
ARG USER_GID=$USER_UID
# Docker GID on the host machine
ARG DOCKER_GID=999

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir -p /home/$USERNAME/.vscode-server /home/$USERNAME/.vscode-server-insiders \
    && chown ${USER_UID}:${USER_GID} /home/$USERNAME/.vscode-server*

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

RUN pip3 install black flake8 mypy pytest google-cloud google-cloud-vision

USER $USERNAME

RUN curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-359.0.0-linux-x86_64.tar.gz | tar -xz -C /home/${USERNAME}/
RUN /home/${USERNAME}/google-cloud-sdk/install.sh -q
#RUN /home/${USERNAME}/google-cloud-sdk/bin/gcloud init

ENV PATH="${PATH}:/home/${USERNAME}/.local/bin"