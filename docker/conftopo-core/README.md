# conftopo-core
A Docker image for the core components of ConfTopo.

* Ubuntu 20.04 with ChimeraX as base image
* Install `pip3` and `git`
* Install essential Python libraries for ConfTopo:
	* `numpy `
	* `pandas`
	* `matplotlib`
	* `streamlit`
	* `biopython`
	* `scikit-tda`
	* `PersistenceCurves`

## Usage
These usage instructions are written specifically for the repository's author to use. Mostly to jog his memory.

1. `cd` into this directory
1. Start Docker, if not already started. For example, on most Linux distros:

	```
	systemctl start docker
	```
1. Build the Docker image: 

	```
	docker build -t maduprey/conftopo-core .
	```
1. Push the image to DockerHub:

	```
	docker push maduprey/conftopo-core:latest
	```

## DockerHub
A prebuilt version of this image can be found on [DockerHub](https://hub.docker.com/repository/docker/maduprey/conftopo-core). Or, use `docker pull maduprey/conftopo-core`.

