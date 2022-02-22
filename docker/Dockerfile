FROM maduprey/chimerax:1.3

# Fix hash sum mismatch issue. For more details, see
# https://forums.docker.com/t/hash-sum-mismatch-writing-more-data-as-expected/45940/2
COPY badproxy /etc/apt/apt.conf.d/99fixbadproxy

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    sudo \
    pip \
    git

# Not strictly necessary:
# Create new non-root user (appuser, ID 1001) and switch to user
# RUN groupadd -g 1001 appuser && \
#     useradd -r -m -u 1001 -g appuser appuser
# USER appuser