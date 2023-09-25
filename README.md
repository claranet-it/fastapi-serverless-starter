# FastAPI Serverless Starter

## Pre-requisites

- Python 3.9.x
- Poetry 1.6.1
- NodeJs 18.x

## Tools and Frameworks

- [x] FastApi
- [x] Uvicorn
- [x] pytest
- [x] pre-commit
- [x] isort
- [x] black
- [x] flake8
- [x] bandit

## Install dependencies

```
poetry install
npm install
```

## Install pre-commit hooks

```
pre-commit install
```

## Commands

Start local server
```
make start-local
```

Start serverless offline
```
make start-serverless-offline
```

Launch tests
```
make test
```

Launch test with coverage
```
make coverage
```

Run pre-commit hooks
```
make pre-commit
```