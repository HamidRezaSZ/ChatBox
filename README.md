# ChatBox

## Installation:

**1. Clone the Repo**

```sh
git clone https://github.com/HamidRezaSaad/ChatBox.git
```

**2. Install Requirements**

```sh
pip install -r requirements.txt
```

**3. Migrate Database**

```sh
python manage.py makemigrations
python manage.py migrate
```

**4. Start Server**

```sh
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/ in a web browser. You will see the webpage.

## How to use admin panel to manage contents

**1. First create a superuser**

```shell
python manage.py createsuperuser
```

**2. Run the server again**

```shell
python manage.py runserver
```

3. Now in web browser visit http://127.0.0.1:8000/admin/ . Login with the superuser username and password you created already.
