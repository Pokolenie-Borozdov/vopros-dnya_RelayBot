# Relay Bot

Простой телеграм-бот, который пересылает сообщения в указанный чат.

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

### Запуск контейнера

```bash
docker run --env-file .env relay-bot
```

## 🖥️ Для архитектуры amd64

Если требуется собрать образ под amd64:

```bash
docker build --platform linux/amd64 -t relay-bot .
```
