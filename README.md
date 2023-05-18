# Instagram clone

## How to deploy to local-machine ?

1. Create virtualenv
2. Install dependencies
    ```
    pip install -r requirements.txt
    ```
3. Apply migrations
    ```
    python3 manage.py migrate
    ```
4. Create superuser
    ```
    python3 manage.py createsuperuser
    ```
5. Run project
    ```
    python3 manage.py runserver 8000
    ```
