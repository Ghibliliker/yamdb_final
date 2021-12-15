[![Django-app workflow](https://github.com/Ghibliliker/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/Ghibliliker/yamdb_final/actions/workflows/yamdb_workflow.yml)
## Проект YaMDb

Где вы ещё видели такую возможность, как написать отзыв на ваш любимый фильм или другое культурное произведение?!
А написать комментарий на отзыв?! А оценить произведения?! верно! Везде!))))
но только у нас это сделано с душой <З
​
​
### Как запустить проект в контейнере:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/api_yamdb.git
```
```
cd infra_sp2/infra
```
2. Выполнить запуск docker-compose:
```
docker-compose up -d --build 
```
3. Подготовка миграций и статики, создание суперпользователя:
```
docker-compose exec web python manage.py migrate
```
```
docker-compose exec web python manage.py createsuperuser
```
```
docker-compose exec web python manage.py collectstatic --no-input
```
4. Шаблон env-файла:
```
DB_ENGINE=***
DB_NAME=***
POSTGRES_USER=***
POSTGRES_PASSWORD=***
DB_HOST=***
DB_PORT=***
```
### Эндпоинты, поддерживаемые API:

* POST /api/v1/auth/signup/    Регистрация нового пользователя
```
{
"email": "string",
"username": "string"
}
```
* POST /api/v1/auth/token/    Получение JWT-токена
```
{
"username": "string",
"confirmation_code": "string"
}
```
* GET /api/v1/users/    Получение списка всех пользователей
* POST /api/v1/users/    Добавление пользователя
```
{
"username": "string",
"email": "user@example.com",
"first_name": "string",
"last_name": "string",
"bio": "string",
"role": "user"
}
```
* GET /api/v1/users/{username}/    Получение пользователя по username
* DELETE /api/v1/users/{username}/     Удаление пользователя по username
* GET /api/v1/users/me/    Получение данных своей учетной записи
* GET /api/v1/categories/    Получение списка всех категорий
* POST /api/v1/categories/    Добавление новой категории
```
{
"name": "string",
"slug": "string"
}
```
* DELETE /api/v1/categories/{slug}/    Удаление категории
* GET /api/v1/genres/    Получение списка всех жанров
* POST /api/v1/genres/    Добавление нового жанра
```
{
"name": "string",
"slug": "string"
}
```
* DELETE /api/v1/genres/{slug}/    Удаление жанра
* GET /api/v1/titles/    Получение списка всех произведений
* POST /api/v1/titles/    
```
{
"name": "string",
"year": 0,
"description": "string",
"genre": [
"string"
],
"category": "string"
}
```
* GET /api/v1/titles/{titles_id}/    Получение информации о произведении
* PATCH /api/v1/titles/{titles_id}/    Частичное обновление информации о произведении
* DELETE /api/v1/titles/{titles_id}/    Удаление произведения
* GET /api/v1/titles/{title_id}/reviews/    Получение списка всех отзывов
* POST /api/v1/titles/{title_id}/reviews/    Добавление нового отзыва
```
{
"text": "string",
"score": 1
}
```
* GET /api/v1/titles/{title_id}/reviews/{review_id}/    Полуение отзыва по id
* PATCH /api/v1/titles/{title_id}/reviews/{review_id}/    Частичное обновление отзыва по id
* DELETE /api/v1/titles/{title_id}/reviews/{review_id}/    Удаление отзыва по id
* GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/    Получение списка всех комментариев к отзыву
* POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/    Добавление комментария к отзыву
```
{
"text": "string"
}
```
* GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/    Получение комментария к отзыву
* PATCH /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/    Частичное обновление комментария к отзыву
* DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/    Удаление комментария к отзыву
​
###### Авторы
Павел Масло, Алексей Файферт, Олег Силкин
