# ConfTopo
![conftopo-core-docker](https://github.com/maduprey/conftopo/actions/workflows/conftopo-core-docker.yml/badge.svg)

 ![ConfTopo](/imgs/conftopo_calmodulin.png)

 Explore topological changes across protein conformational changes.


## Running the app
ConfTopo runs as a [Streamlit](https://streamlit.io/) app. The preferred method of running the application is within a Docker container. Optionally, instructions are provided for running locally on macOS. 

Regardless of the execution modality, first clone this repository:
```
git clone https://github.com/maduprey/conftopo.git
```

## Docker

### Setup
1. Install [Docker](https://www.docker.com/).
1. `cd` into the repository.

### Usage
1. Start Docker. For example, on most Linux distros:
	```
	systemctl start docker
	```
1. Build the Docker image: 
	```
	docker build -f docker/Dockerfile -t conftopo .
	```
1. Run the Docker container:
	```
	docker run -p 8501:8501 conftopo
	```
1. In your browser, navigate to the Streamlit app at [http://localhost:8501/](http://localhost:8501/)


## Local

### Setup
1. [Download](https://www.cgl.ucsf.edu/chimerax/download.html) and install UCSF ChimeraX 1.3. If the ChimeraX executable is installed somewhere else, edit the path `/Applications/ChimeraX-1.3.app/Contents/MacOS/ChimeraX` in `chimerax.py`.

1. `cd` into this repository.
1. Using [conda](https://docs.conda.io/), create and activate a virtual environment `conftopo` with pip installed:
	```
	conda create -n conftopo python=3.8
	conda activate conftopo
	conda install pip
	```
1. Install the required Python packages:
	```
	pip install -r requirements.txt
	```

### Usage
1. Start the Streamlit app:
	```
	streamlit run run_conftopo.py
	```
1. In your browser, navigate to [http://localhost:8501/](http://localhost:8501/)