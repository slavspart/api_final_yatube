# api_final
Учебный проект API для соцсети Yatube.
Выполнен студентом Яндекс Практикума Михайловым Святославом.

### Возможности:

Предоставляет возможность получения в формате JSON информации о постах, группах, комментариях, подписках соцсети Yatube. Для получения большей части информации необходимо авторизоваться и получить токен. Подробная документация доступна после запуска сервера на странице http://127.0.0.1:8000/redoc/.

### Зависимости:
Проект основан на следующих технологиях:
* python 3.7.9
* Django 2.2.16
* djangorestframework 3.12.4


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/slavspart/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate или source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Документация с возможностями проекта:
```
http://127.0.0.1:8000/redoc/



