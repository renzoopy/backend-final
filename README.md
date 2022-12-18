# venta-productos

API para el sistema de ventas de productos a clientes - 2do Final BACKEND 

## Requerimientos

-   Python >= 3.7
-   Pipenv
-   PostgreSQL >= 10

## Entorno de desarrollo

1. Crea una base de datos para el proyecto:

    ```bash
    DROP DATABASE IF EXISTS ventas;
    CREATE DATABASE ventas;
    GRANT CONNECT ON DATABASE ventas TO ventas;
    ```

2. En la carpeta raíz, crea un archivo `.env` con el siguiente contenido:

    ```
        debug = True
        secret_key = supersecretkey
        allowed_hosts = *
        db_user = ventas
        db_password = ventas
        db_name = ventas
        db_host = 127.0.0.1
        db_port = 5432
        email_host = emaillhost
        email_from = emailfrom
        email_port = emailport
        email_user = emailuser
        email_password = emailpassword
        frontend_url = frontenturl
        email_use_ssl = true
        email_use_tls = false

    ```

3. Instala las dependencias del proyecto:

    ```bash
    pipenv install
    ```

4. Ejecuta las migraciones y corra el script de llenado de base de datos:

    ```bash
    pipenv run python manage.py migrate
    pipenv run python manage.py populatecore
    ```

5. Ejecuta el servidor de desarrollo:

    ```bash
    pipenv run python manage.py runserver
    ```

6. Usuario administrador
```bash
    user: admin
    password: admin
    ```
    
