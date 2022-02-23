FROM maduprey/chimerax:1.3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    python3-pip \
    git

# Install pip packages
RUN pip3 install --upgrade pip \
    && pip3 install --no-use-pep517 bcrypt \
    && pip3 install numpy \
        pandas \
        matplotlib \
        streamlit \
        biopython \
        scikit-tda \
    && pip3 install git+https://github.com/azlawson/PersistenceCurves.git

# RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
#     python3-pip \
#     git \
#     libcairo2-dev \
#     libgirepository1.0-dev

# # Install pip packages
# RUN pip3 install --upgrade pip \
#     && pip3 install --no-use-pep517 bcrypt \
#     && pip3 install -r /conftopo/requirements.txt \
#     && pip3 install git+https://github.com/azlawson/PersistenceCurves.git