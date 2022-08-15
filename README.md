# Certificate Manager

## Dependencies
    - Python: tested with version 3.9.12
    - Flask: tested with version 2.2.2
    - Pytest(only for the testsuite): tested with version 7.1.2
    - Docker(only if containerization is required): tested with version 20.10.17

## Installation
```bash
git clone <REPO-URL>
```

```bash
python -m pip install -r requirements.txt
```

## Running The App

One can either let the app run on a native system by:
```bash
python main.py
```

or in a docker container:
```bash
docker build -t <DOCKER_IMAGE_NAME> .
docker run -d -p 5000:5000 <DOCKER_IMAGE_NAME>
```

or let the management of containers be done by `docker-compose`:
```bash
docker-compose up -d
```

## Viewing The App

Go to `http://127.0.0.1:5000`
