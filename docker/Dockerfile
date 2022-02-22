FROM maduprey/chimerax:1.3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    sudo \
    pip \
    git

# Not strictly necessary:
# Create new non-root user (appuser, UID 1001) and switch to user
# RUN groupadd -g 1001 appuser && \
#     useradd -r -m -u 1001 -g appuser appuser
# USER appuser