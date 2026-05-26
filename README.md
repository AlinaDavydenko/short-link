# URL Shortener

A simple URL shortening service built with FastAPI, SQLAlchemy and Docker. 

## Features

- Shorten long URLs to short codes
- Redirect to original URL by short code
- Track click count for each short URL

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- uvicorn
- Docker

## Project Structure

```
url_shortener/
├── app/
│   ├── db_core/
│   │   ├── db_connection.py
│   │   ├── models.py
│   │   ├── database.py
│   │   └── session.py
│   ├── tests/
│   │   └── test_router.py
│   ├── main.py
│   ├── router.py
│   ├── schemas.py
│   └── utils.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/AlinaDavydenko/short-link
cd url_shortener
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running
### Local

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up --build
```

Open http://localhost:8000/docs to see the API documentation.

## API

### POST /shorten
Shorten a long URL.

Request:
```json
{"original_url": "https://example.com"}
```

Response:
```json
{
  "original_url": "https://example.com",
  "short_code": "aB3kR9",
  "clicks": 0
}
```

### GET /{short_code}
Redirect to original URL by short code.

Returns HTTP 307 redirect to original URL.
Returns HTTP 404 if short code not found.

## Testing

Run tests:
```bash
pytest app/tests/test_router.py -v
```
