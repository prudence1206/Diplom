##Как пускануть проект:


- install all libraries 
```
  pip install -r requirements.txt
```
- make migrations and run server
```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```
- run redis server
```
  redis-server
  redis-cli
```
- run celery for async requests
```
  python -m celery -A diploma  worker
```

## Запуск тестов:

- create connection with postgress DB
```
sudo -u posgress sql <db_name_in_settings>
```
- after creatin DB, create user
```
ALTER USER <db_user_in_settings> CREATEDB
```
- run tests with command
```
python manage.py test backend
```
