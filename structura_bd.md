
---

# 📚 Структура базы данных 

## 1. Пользователи (`User`)

Используем встроенную модель Django (`django.contrib.auth.models.User`).

| Поле         | Тип           | Ограничения/Связи                            |
| ------------ | ------------- | -------------------------------------------- |
| username     | CharField     | `unique=True`, `max_length=150`              |
| email        | EmailField    | `unique=True` (часто используется для входа) |
| password     | CharField     | `max_length=128`                             |
| date\_joined | DateTimeField | `auto_now_add=True`                          |
| is\_active   | BooleanField  | `default=True`                               |
| is\_staff    | BooleanField  | `default=False`                              |

---

## 2. Категории (`Category`)

| Поле        | Тип       | Ограничения/Связи         |
| ----------- | --------- | ------------------------- |
| name        | CharField | `max_length=100`          |
| slug        | SlugField | `unique=True`             |
| description | TextField | `blank=True`, `null=True` |

Описание: Категории помогают группировать посты (например, «Новости», «Python»).

---

## 3. Посты (`Post`)

| Поле          | Тип           | Ограничения/Связи                                     |
| ------------- | ------------- | ----------------------------------------------------- |
| title         | CharField     | `max_length=200`                                      |
| slug          | SlugField     | `unique=True`                                         |
| content       | TextField     | —                                                     |
| author        | ForeignKey    | связь с `User`, `on_delete=CASCADE`                   |
| category      | ForeignKey    | связь с `Category`, `on_delete=SET_NULL`, `null=True` |
| created\_at   | DateTimeField | `auto_now_add=True`                                   |
| updated\_at   | DateTimeField | `auto_now=True`                                       |
| is\_published | BooleanField  | `default=True`                                        |
| views\_count  | IntegerField  | `default=0`                                           |

Описание: Основная сущность блога — статья. Содержит заголовок, текст, автора, дату публикации и статус.

---

## 4. Комментарии (`Comment`)

| Поле        | Тип           | Ограничения/Связи                                                 |
| ----------- | ------------- | ----------------------------------------------------------------- |
| post        | ForeignKey    | связь с `Post`, `on_delete=CASCADE`                               |
| author      | ForeignKey    | связь с `User`, `on_delete=CASCADE`                               |
| content     | TextField     | —                                                                 |
| created\_at | DateTimeField | `auto_now_add=True`                                               |
| parent      | ForeignKey    | связь с `Comment`, `on_delete=CASCADE`, `null=True`, `blank=True` |

Описание: Комментарии к постам. Поддерживают вложенность через поле `parent`.

---

## 5. Теги (`Tag`)

| Поле  | Тип             | Ограничения/Связи |
| ----- | --------------- | ----------------- |
| name  | CharField       | `max_length=50`   |
| slug  | SlugField       | `unique=True`     |
| posts | ManyToManyField | связь с `Post`    |

Описание: Теги для гибкой классификации постов (например, «Django», «WebDev»).

---

## 6. Лайки (`Like`)

| Поле        | Тип           | Ограничения/Связи                   |
| ----------- | ------------- | ----------------------------------- |
| post        | ForeignKey    | связь с `Post`, `on_delete=CASCADE` |
| user        | ForeignKey    | связь с `User`, `on_delete=CASCADE` |
| created\_at | DateTimeField | `auto_now_add=True`                 |

Описание: Система оценки. Один пользователь может лайкнуть пост только один раз (обычно ограничивается через `UniqueConstraint(post, user)`).

---

# 🧩 Визуальная схема (с типами полей)

```
User (Django)
   ├── username (Char, unique)
   ├── email (Email, unique)
   └── password (Char)
        │
        ├── Post
        │    ├── title (Char)
        │    ├── content (Text)
        │    ├── author (FK User)
        │    ├── category (FK Category)
        │    ├── created_at (DateTime)
        │    └── is_published (Bool)
        │
        ├── Category
        │    ├── name (Char)
        │    └── slug (Slug, unique)
        │
        ├── Tag
        │    ├── name (Char)
        │    └── slug (Slug, unique)
        │    └── posts (M2M Post)
        │
        ├── Comment
        │    ├── post (FK Post)
        │    ├── author (FK User)
        │    ├── content (Text)
        │    └── parent (FK Comment, null)
        │
        └── Like
             ├── post (FK Post)
             └── user (FK User)
```

---
