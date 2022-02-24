# ConfTopo
 Topological changes across protein conformational changes.


## Usage
The preferred method of running is using Docker. However, it is possible to run locally on macOS. Instructions for both approaches are provided.

Regardless of the approach taken, it is first necessary to clone this repository and `cd` into it:

```
git clone https://github.com/maduprey/conftopo.git
```

### Docker
1. Install [Docker](https://www.docker.com/)

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


### Local

1. Assuming all the necessary Python libraries are installed and the repo is the current directory, run Streamlit:

	```
	streamlit run run_conftopo.py
	```
1. In your browser, navigate to [http://localhost:8501/](http://localhost:8501/)