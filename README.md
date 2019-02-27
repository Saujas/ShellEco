# ShellEco Website

### Clone this repo

```bash
git clone https://github.com/Saujas/ShellEco
```

### Setting up the virtual environment with venv

- Refer this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)

### Creating a virtual environment

```bash
cd ShellEco
python3 -m venv env
source env/bin/activate
```

### Installing requirements

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### To create a superuser to login to admin ('admin/')

```bash
python3 manage.py createsuperuser
```

### To run the server

```bash
python3 manage.py runserver 0.0.0.0:8000
