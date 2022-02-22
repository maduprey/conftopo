FROM ubuntu:20.04

COPY ucsf-chimerax_1.3ubuntu20.04_amd64.deb /

# Need this to fix a wonky issue with URLS in apt
COPY badproxy /etc/apt/apt.conf.d/99fixbadproxy

# RUN apt-get update && apt-get install -y \
#     sudo \
#     pip \
#     git

# RUN apt-get update

# Passing in responses that set time-zone to Denver, CO
RUN apt-get update && printf '2\n47\n47\n' | \ 
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    /ucsf-chimerax_1.3ubuntu20.04_amd64.deb

# # Create new non-root user (appuser, ID 1001) and switch to user
# RUN groupadd -g 1001 appuser && \
#     useradd -r -m -u 1001 -g appuser appuser
# USER appuser