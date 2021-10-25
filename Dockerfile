FROM python:3.7.9

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.11

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install $(echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /app

CMD poetry run vehicle-listener
