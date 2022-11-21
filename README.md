# Drone

## Installation / local development

1. Create a new Python virtual environment:
    ```shell
    python3 -m virtualenv venv
    source ./venv/bin/activate
    ```
    Note: See https://virtualenv.pypa.io/en/latest/installation.html if `virtualenv` is not installed in your local.

2. Install requirements:
   ```shell
   pip install -r requirements.txt
   ```
   
3. To run any command:
   ```shell
   python manage.py <runserver|migrate|...any cmd>
   ```
