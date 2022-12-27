

<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/e-backend-.git
# After cloning, move into the directory 
# having the project files 
```
#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate.bat

# Linux and Mac
source env/bin/activate

```
#### Install all the project Requirements

```bash

pip install -r require.txt

```
#### Apply migrations and create your superuser (follow the prompts)

```bash

# Apply make migrations
python manage.py makemigrations

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

```

#### Run the development server

```bash
# run django development server
python manage.py runserver

```
Now we are good to Go . We can check the [127.0.0.1:8000](http://127.0.0.1:8000) <br> for The root API documention.
<br>


<h2 align="center"> Project Structure</h2>
<br>

```bash 


    mainConfig/  #Root Config folder
        |-- __init__.py
        |__ settings/
            |-- base.py # base settings
            |-- development # development settings)
        |-- urls.py (Root URL file)
        |-- wsgi.py
        |-- asgi.py


    structure   # All the APPs will be under on it
        |-- __init__.py
        |__ core / 
            |-- baes_models.py # Mixxin abstruct models 
            |-- base_serialzier.py # Base API 
        |__ accounts/ 
            |-- __init.py
            |__ models / # database folder  
                |-- base.py # Base User config
            |__ tests / # tests folder 
                |-- __init__.py
                |-- urls_tests.py # URLs test case
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ invenory /
            |-- __init__.py
            |-- models.py # Inventory database file
            |__ views # Views folder
                |-- category view # category views
                |-- products view # products views 
                |-- dependency view # dependency views
            |__ tests / # tests folder 
                |-- __init__.py
                |-- urls_tests.py # URLs test case
            |__ api / # API folder
                |-- category api 
                |-- dependency api
                |-- products api
            |-- urls.py # Code list URL file)
            |-- admin.py

    |-- manage.py
    |-- .env  
    |-- .gitignore
    |-- db # development database 
    |-- require.txt # package dependency file
    

```