install:
	poetry install

run:
	poetry run vehicle-listener

test:
	poetry run pytest -v -vv

lint:
	poetry run flake8 vehicle_listener
