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
	```bash
	systemctl start docker
	```
1. Build the Docker image: 
	```bash
	docker build -f docker/Dockerfile -t conftopo .
	```
1. Run the Docker container:
	```bash
	docker run -p 8501:8501 conftopo
	```
1. In your browser, navigate to the Streamlit app at [http://localhost:8501/](http://localhost:8501/)


## Local

### Setup
1. [Download](https://www.cgl.ucsf.edu/chimerax/download.html) and install UCSF ChimeraX 1.5. If the ChimeraX executable is installed somewhere else, edit the path `/Applications/ChimeraX-1.5.app/Contents/MacOS/ChimeraX` in `chimerax.py`.

1. `cd` into this repository.
1. Using [conda](https://docs.conda.io/), create and activate a virtual environment `conftopo` with pip installed:
	```bash
	conda create -n conftopo python=3.8
	y # Accept any new packages that will be installed
	conda activate conftopo
	```
1. Install the required Python packages:
	```bash
	pip install -r requirements.txt
	```

### Usage
1. Start the Streamlit app:
	```bash
	streamlit run run_conftopo.py
	```
1. In your browser, navigate to [http://localhost:8502/](http://localhost:8502/)

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`conftopo` was created by Michael Duprey. It is licensed under the terms of the MIT license.

## Credits

`conftopo` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
