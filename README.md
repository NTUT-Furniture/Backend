# Backend

## setup environment on windows(optional)

```bash
python3 -m venv venv
venv/Scripts/activate
```

## run uvicorn server

```bash
pip install -r requirements.txt
python3 main.py
```

## Docker

### run

For frontend development, you can run the backend and Database with Docker. To do so, follow the steps below:

   ```bash
   docker-compose  -f docker-compose-ALL.yml up -d
   ```

For backend development, you can run the backend with Docker. To do so, follow the steps below:

   ```bash
   docker-compose -f docker-compose-DB.yml up -d
   ```

### clean all

make sure no container is running

   ```bash
   docker system prune -a
   ```

### PyCharm Hacks

~~For GUI freaks fellows~~, you can run the backend with PyCharm's Run/Debug Configuration . To do so, follow the steps
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
