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

   ```bash
   docker-compose up
   ```

### clean all

make sure no container is running

   ```bash
   docker system prune -a
   ```

### PyCharm Hacks

~~For GUI freaks fellows~~, you can run the backend with PyCharm's Run/Debug Configuration . To do so, follow the steps
below:

`Run DB`: This hosts the database.

`Run Backend`: This hosts the database and backend, then automatically opens the browser
with http://localhost:8000/api/docs.

Please note:

* When executing `Run Backend` for the first time, it might fail initially due to the time taken for building the Docker
  container. Simply wait until the Docker's output signals readiness, then proceed to run it again.

* When initiating the first run for `Run Backend`, there will be a pop-up(shown below) asking you to select a Python
  interpreter as I
  comment out those config, please select the Python interpreter you have created for this project.<br>
  ![](https://ppt.cc/fDYK7x)

  In case you have not created a Python interpreter, please do so by following the steps below:
    1. Open the Settings/Preferences dialog box, and then select `Project: Backend` | Python Interpreter.
    2. In the Python Interpreter page, click the gear icon and select Add.
    3. In the left-hand pane of the Add Python Interpreter dialog box, select Virtualenv Environment.
    4. Specify the location of the new virtual environment in the text field, or click and find location in your file
       system.
    5. Select the base interpreter(Python 3.10.x is recommended) from the list, or click and find location in your file
       system.
    6. Click OK to finish the process.
    7. Click OK to complete the task.
    8. Proceed to select the newly created Python interpreter in the Configuration settings.
    9. Click OK to complete the task.
    10. Run `Run Backend` again.
