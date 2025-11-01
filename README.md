# Убегающая кнопка - DevSecOps Edition

Веб-приложение с убегающей кнопкой + API для статистики.

## Версия: 1.1.0

### Что нового в 1.1.0:
- ✅ API endpoints для статистики (`/api/stats`, `/api/attempt`, `/api/win`)
- ✅ Health check endpoint (`/health`)
- ✅ Логирование всех действий
- ✅ Безопасность: SECRET_KEY через переменные окружения
- ✅ Конфигурация через .env файл
- ✅ Отслеживание попыток и побед в реальном времени

## Установка

```bash
# Установить зависимости
pip install -r requirements.txt

# Создать .env файл
cp .env.example .env

# Изменить SECRET_KEY в .env на свой
```

## Запуск

```bash
python app.py
```

Приложение будет доступно на `http://localhost:5001`

## API Endpoints

- `GET /` - Главная страница
- `GET /api/stats` - Получить статистику (попытки, победы, сессии)
- `POST /api/attempt` - Залогировать попытку поймать кнопку
- `POST /api/win` - Залогировать успешное согласие
- `GET /health` - Health check для мониторинга

## Примеры API запросов

```bash
# Получить статистику
curl http://localhost:5001/api/stats

# Health check
curl http://localhost:5001/health
```

## Безопасность

- ✅ SECRET_KEY вынесен в переменные окружения
- ✅ Debug режим отключается в production
- ✅ .env файл в .gitignore
- ✅ Логирование для аудита

## Changelog

### 1.1.0 (2025-11-01)
- Добавлены API endpoints
- Добавлено логирование
- Улучшена безопасность
- Добавлена конфигурация через .env

### 1.0.0
- Первая версия с убегающей кнопкой

