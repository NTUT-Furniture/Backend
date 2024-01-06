# Backend

## setup environment on windows(optional)

```bash
python3 -m venv venv
venv/Scripts/activate
```

## Docker

pull the image if it's not present, and run as services in detach mode
```
docker compose up -d
```

stop the services
```
docker compose stop
```

start the services
```
docker compose start
```

remove the containers
```
docker compose down
```

### PyCharm Hacks

~~For GUI freak fellows~~, you can run the backend with PyCharm's Run/Debug Configuration . To do so, follow the steps
below:

* Docker configurations

    * `Run DB`: This hosts the database.

    * `Run ALL`: This hosts the database and backend.

* Python configurations
    * `Run Backend`: This hosts the database and backend, then automatically opens the browser
      with http://localhost:8000/api/docs.

Please note:

* When executing `Run Backend` or `Run ALL`for the first time, it might fail initially due to the time taken for
  building the Docker
  container. Simply wait until the Docker's output signals readiness, then proceed to run it again.
