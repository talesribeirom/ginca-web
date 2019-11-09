# Ginca-Web (Back-End)

### Tecnologia Utilizadas

* Django 2.2
* Python 3.5+
* Postgres 9+

### Instalação


* Executando no Linux:

      virtualenv -p python3 env

      source env/bin/activate

      pip install -r requirements.txt
      
      pip install django-crispy-forms (somente necessário no projeto de teste)

      python manage.py migrate

      python manage.py createsuperuser

      python manage.py runserver

* Executando no Windows:

      virtualenv -p py env

      env/Scripts/activate

      pip install -r requirements.txt
      
      pip install django-crispy-forms (somente necessário no projeto de teste)

      python manage.py migrate

      python manage.py createsuperuser

      python manage.py runserver

### Padronização BD

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ginca_web',
            'USER': 'usr_gincaweb',
            'PASSWORD': 'pwd_gincaweb',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
