FROM ubuntu:20.04

COPY ucsf-chimerax_1.3ubuntu20.04_amd64.deb /

RUN apt-get update && apt-get install -y \
    sudo \
    pip \
    git

# Some issue here with a hash sum mismatch
#RUN apt-get install -y /ucsf-chimerax_1.3ubuntu20.04_amd64.deb

# Create new non-root user (appuser, ID 1001) and switch to user
# RUN groupadd -g 1001 appuser && \
#     useradd -r -u 1001 -g appuser appuser
# USER appuser