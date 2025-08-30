### Экспорт данных в фикстуру

```shell
python manage.py dumpdata > ./fixtures/blog_app_all_data.json
```

### Экспорт данных в фикстуру в читаемом виде

```shell
python manage.py dumpdata --indent 4 > ./fixtures/blog_app_all_data.json
```

### Экспорт данных приложения blog_app в фикстуру в читаемом виде

```shell
python manage.py dumpdata blog_app --indent 4 > ./fixtures/blog_app_all_data.json
```

### Экспорт данных модели Post из приложения blog_app в фикстуру в читаемом виде

```shell
python manage.py dumpdata blog_app.Post --indent 4 > ./fixtures/blog_app_all_data.json

```

### Импорт данных из фикстуры

```shell
python manage.py loaddata ./fixtures/blog_app_all_data.json
```

# Тестовое наполнение базы данных

В начале загружаем users_fixtures.json, потом blog_app_all_data.json
