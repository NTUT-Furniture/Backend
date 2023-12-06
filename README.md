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

## environment variables

1. You have the option to manage your environment variables using two methods:
   Using a .env file: Create a .env file in the root directory of your project and populate it with your environment
   variables, as shown below:
    ```text
    # .env
    DB_HOST=<your-db-host>
    DB_USER=<your-db-user>
    DB_PASSWORD=<your-db-password>
    DB_DATABASE=<your-database-name>
    SECRET_KEY=<your-secret-key>
    ALGORITHM=<your-algorithm>
    ```
2. Using your IDE's run configurations: Another option is to set the necessary environment variables directly in your
   IDE's run configuration. Please refer to the documentation specific to your IDE for this process.
