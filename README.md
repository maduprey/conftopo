# ConfTopo
 Topological changes across protein conformational changes.

## First time setup
1. Install [Docker](https://www.docker.com/).

## Usage
1. Clone this repository and `cd` into it:

	```
	git clone https://github.com/maduprey/conftopo.git
	```
1. Start Docker, if not already started. For example, on most Linux distros:

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
1. In your browser, navigate to [http://localhost:8501/](http://localhost:8501/)


