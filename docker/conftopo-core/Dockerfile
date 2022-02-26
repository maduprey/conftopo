FROM maduprey/chimerax:1.3

COPY /requirements.txt /requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    python3-pip \
    git

# Install pip packages
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Install pip packages
# RUN pip3 install --upgrade pip \
#     && pip3 install --no-use-pep517 bcrypt \
#     && pip3 install numpy \
#         pandas \
#         matplotlib \
#         streamlit \
#         biopython \
#         scikit-tda \
#         py3dmol \   
#         git+https://github.com/azlawson/PersistenceCurves.git