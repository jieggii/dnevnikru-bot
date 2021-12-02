# dnevnikru-bot
Селфхостед VK бот для вашей классной беседы, работающий с API [dnevnik.ru](https://dnevnik.ru). 

## Команды:
* `/help` - список команд
* `/today` - расписание на сегодня
* `/tommorow` - расписание на завтра
* `/ht` - все домашние задания, начиная с сегодняшнего дня

## Зависимости
* Python 3.9+
* poetry
* make
* docker

## Использование
### Настройка
Скопируйте содержимое `.env.example` в файл `.env`: 
```shell
$ cp .env.example .env
```
В нем будут храниться необходимые для работы бота переменные среды:
```dotenv
BOT_TOKEN=              # access token бота
BOT_GROUP_ID=           # group id бота
BOT_DOMAIN=             # domain (юзернейм) бота
BOT_PEER_IDS=*          # Разрешенные peer_id. Можно указать один или
                        # несколько штук через запятую. Бот будет реагировать
                        # только на сообщения, написанные в заданных беседах.
                        # Также можно присвоить значение "*", тогда бот будет 
                        # реагировать на сообщения из всех бесед.

DNEVNIKRU_LOGIN=        # логин от dnevnik.ru
DNEVNIKRU_PASSWORD=     # пароль от dnevnik.ru
DNEVNIKRU_SCHOOL_ID=    # school_id в dnevnik.ru
DNEVNIKRU_EDU_GROUP=    # edu_group в dnevnik.ru
```

### Запуск
Удобнее всего запускать бота в докер-контейнере:
```shell
$ docker build --tag dnevnikru-bot .  # собираем контейнер
$ docker run dnevnikru-bot:latest     # и запускаем его
```

## TODO:
- [ ] Автоматическая отправка расписания уроков
- [ ] Показывать пользователю время урока
