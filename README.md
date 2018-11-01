# Cloudtables

A simple web based table administration platform for small food serving places.

## Requirements
- mkvirtualenv
- python3 / pip3
- django

## Installation

Clone this repository.

### Development 

```bash
$ sudo apt install mkvirtualenv
$ source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
$ mkdir ~/.Envs/
$ export WORKON_HOME=~/.Envs/
$ mkvirtualenv -p /usr/bin/python3 VIRTUALENV_NAME
$ deactivate
$ nano -w ~/.Envs/VIRTUALENV_NAME/bin/postactivate
```

Add the following lines to ~/.Envs/VIRTUALENV_NAME/bin/postactivate :
```bash
export DJANGO_SETTINGS_MODULE='cloudtables.settings.development' 
```

Also edit ~/.Envs/VIRTUALENV_NAME/bin/predeactivate and add the following line:
```bash
unset DJANGO_SETTINGS_MODULE
```

Then run:
```bash
$ workon VIRTUALENV_NAME
$ pip install -r requirements
$ git clone https://github.com/microphone-mathematics/create-django-postgres-db.git ~/create-psql-db/
$ sh ~/create-psql-db/create_psql_database.sh cloudtables
```

After that edit PROJECT_ROOT/cloudtables/settings/base.py and look for the database configuration and set username to 'cloudtablespsql' and password to the one you just choose when executing create_psql_database.sh

Finishing steps:
```bash
$ ./manage.py migrate
$ ./manage.py runserver
```

You should now have a working development server at http://localhost:8000
