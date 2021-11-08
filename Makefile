fmt:
	poetry run isort app/
	poetry run black app/

lint:
	poetry run flake8 app/

run-local:
	poetry run dotenv -f .env run python -m app

docker-build:
	docker build --tag dnevnikru-bot .

docker-run:
	docker run dnevnikru-bot:latest

docker-deploy:
	docker run -d dnevnikru-bot:latest