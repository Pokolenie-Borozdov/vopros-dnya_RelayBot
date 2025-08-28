# Relay Bot

Простой телеграм-бот, который отвечает на все сообщения.

## ⚙️ Настройка

Перед запуском необходимо создать файл `.env` в корне проекта и указать в нём переменные окружения:

```env
TELEGRAM_BOT_TOKEN=your_token
TARGET_CHAT_ID=your_chat_id
````

* `TELEGRAM_BOT_TOKEN` — токен, полученный у [@BotFather](https://t.me/BotFather).
* `TARGET_CHAT_ID` — ID чата или пользователя, куда бот будет отправлять сообщения.

## 🚀 Запуск через Docker

### Сборка образа

```bash
docker build -t relay-bot .
```

## 🖥️ Для архитектуры amd64

Если требуется собрать образ под amd64:

```bash
docker build --platform linux/amd64 -t relay-bot .
```

## 📦 Создание tar-архива образа

Чтобы экспортировать образ в файл `.tar`:

```bash
docker save -o relay-bot.tar relay-bot:latest
```

* `relay-bot.tar` — имя создаваемого файла.
* `relay-bot:latest` — имя и тег образа.

Если хотите сжать для экономии места:

```bash
docker save relay-bot:latest | gzip > relay-bot.tar.gz
```

Для загрузки на другой хост:

```bash
docker load -i relay-bot.tar
# или для gzip
gunzip -c relay-bot.tar.gz | docker load
```

### Запуск контейнера

```bash
docker run relay-bot
```
