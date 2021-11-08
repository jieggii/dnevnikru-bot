FROM python:3.9
RUN pip install poetry==1.1.11

WORKDIR /bot/
COPY pyproject.toml poetry.lock* /bot/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi
COPY app .env /bot/

ENTRYPOINT ["dotenv", "-f", ".env", "run", "python", "-m", "app"]