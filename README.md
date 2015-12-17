AskPupkin
=========

Это django-приложение, реализующее очень простой stackoverflow.

Написано для курса [основ веб-разработки](https://track.mail.ru/curriculum/program/discipline/2/) в рамках [технотрека](track.mail.ru).


Заметки для преподавателя
-------------------------

В проекте есть пара нестандартных ходов, которые стоит учесть при запуске.

1. Bootstrap поставлен с помощью [bower](http://bower.io/). Чтобы он поставился также, как у меня, нужно выполнить `bower install` в папке `static`.

2. SECRET_KEY в settings.py читается из файла secret_key.txt, который лежит директорией выше, чем сам проект.

Ещё стоит обратить внимание, что у проекта, действительно, есть зависимости кроме чистой django. Как положено, лежат в requirements.txt.

Отмечу, что настройки nginx, которые лежат в репозитории — это именно те настройки, которые я использую для запуска. Глобальные настройки nginx на моём компьютере состоят просто из include для этого файла.

О, ещё иногда я использую DEBUG = False в settings.py, поэтому разработческий сервер django может отказаться показывать статику.


Выполнение пунктов д/з
----------------------

Здесь я отмечаю, какие пункты д/з я считаю выполненными. Текущая сумма баллов:

```
17 + (11 + 12 + 1 + 4 + 0) / 2 = 31 (неуд)
```

Ниже подробнее по каждому д/з.

###ДЗ 1 «Настройка серверов»

Выполнено на **17/17**, зачтено вовремя без понижающих коэфицентов.

**5/5** Настройка nginx для отдачи статического контента

+ **3/3** общее
+ **1/1** локейшен /upload/ приоритетнее статики
+ **1/1** проксирование

**2/2** Настройка gunicorn для запуска wsgi приложений

+ **2/2** общее

**3/3** Оценка производительности nginx и gunicorn

+ **1/1** отдача статики
+ **1/1** запуск WSGI
+ **1/1** запуск WSGI с проксированием через nginx

**3/3** Создание hello-world WSGI приложения

+ **2/2** собственно hello-world
+ **1/1** отображение списка GET, POST и других параметров

**4/4** Создание django hello-world приложения

+ **1/1** создание структуры проекта
+ **1/1** создание hello-world view
+ **2/2** использование шаблонизатора

###Д3 2 «Статическая вёрстка»

Выполнено на **11/17**, будет зачтено с понижением оценки в 2 раза за просрок.

**5/5** Верстка общего вида (layout) страницы

+ **1/1** общий вид: 2 колонки, header, footer
+ **1/1** правая колонка
+ **1/1** терпимые отступы
+ **1/1** блок авторизованного юзера
+ **1/1** поисковая строка и логотип

**3/3** Верстка листинга вопросов

+ общий вид (паддинги, аватарка)
+ кнопки лайков
+ тэги, счетчики ответов, остальное

**0/3** Верстка страницы вопроса

+ **0/1** общий вид
+ **0/1** чекбокс “правильный ответ”, кнопки лайков
+ **0/1** форма ответа

**1/3** Верстка формы добавления вопроса

+ **1/2** общий вид
+ **0/1** сообщения об ошибках

**2/3** Верстка форм логина и регистрации

+ **2/2** общий вид
+ **0/1** аватарка и сообщения об ошибках

###ДЗ 3 «Django»

Выполнено на **12/18**, будет зачтено с понижением оценки в 2 раза за просрок.

**4/4** Правильно поставить django

+ **1/1** использование virtualenv, pip
+ **1/1** запуск django через gunicorn
+ **1/1** нет проблем с правами доступа
+ **1/1** структура папок (env, папка проекта, collected_static, uploads итд)

**1/5** Создать views и шаблоны для основных страниц

+ **0/1** главная (список вопросов)
+ **0/1** страница вопроса (список ответов)
+ **0/1** страница добавления вопроса 
+ **0/1** форма регистрации
+ **1/1** форма входа

**2/4** Создать urls.py для всех страниц

+ **1/2** Собственно urls.py
+ **1/2** Именованные маршруты

**5/5** Авторизация

+ **1/1** Использование стандартных view
+ **1/1** Вход на сайт
+ **1/1** Возврат на исходную страницу
+ **1/1** Выход с сайта
+ **1/1** Отображать текущего пользователя в шапке


###ДЗ 4 «Работа с базой данных»

Выполнено на **1/14**, будет зачтено с понижением оценки в 2 раза за просрок.

**0/5** Проектирование моделей

+ **0/1** правильные адекватные типы данных и внешние ключи
+ **0/1** своя модель пользователя
+ **0/1** таблицы тэгов, лайков
+ **0/2** query-setы для типовых выборок: новые вопросы, популярные, по тэгу

**0/3** Наполнение базы тестовыми данными

+ **0/2** наполнение данными
+ **0/1** использование django management commands

**1/3** Отображение списка вопросов

+ *1/1* список новых вопросов
+ *0/1* список популярных
+ *0/1* список вопросов по тэгу

**0/3** Отображение страницы вопроса

+ *0/2* общее
+ *0/1* ещё один балл

###ДЗ 5 «Интерактивный сайт»

Выполнено на **4/17**, будет зачтено с понижением оценки в 2 раза за просрок.

**4/5** Добавление вопроса

+ **1/1** общее
+ **1/1** проверка авторизации, csrf, метода запроса
+ **0/1** добавление тэгов
+ **1/1** отображение ошибок
+ **1/1** правильные редиректы

**0/6** Добавление ответа

+ **0/1** общее
+ **0/1** проверка авторизации, csrf, метода запроса
+ **0/1** редирект на добавленный ответ
+ **0/3** отправка почты автору вопроса

**0/3** Лайки вопросов и ответов

+ **0/1** общее
+ **0/1** проверка авторизации, csrf, метода запроса, авторства
+ **0/1** ajax

**0/3** Отметка “правильный ответ”

+ **0/1** общее
+ **0/1** проверка авторизации, csrf, метода запроса, авторства
+ **0/1** ajax

###ДЗ 6 «Дополнительные функции»

Выполнено на **0/16**, будет зачтено с понижением оценки в 2 раза за просрок.

**0/8** Полнотекстовый поиск

+ **0/2** настройка стандартной библиотеки django - sphinx
+ **0/2** настройка индексатора sphinx
+ **0/2** страница полнотекстового поиска
+ **0/2** одновременный поиск по вопросам и ответам

**0/4** Блок популярные тэги

+ **0/2** правильный расчет тэгов
+ **0/2** предварительный расчет по cron
	- **0/1** просто кеширование

**0/4** Блок лучшие пользователи

+ **0/2** правильный расчет пользователей
+ **0/2** предварительный расчет по cron
	- **0/1** просто кеширование

