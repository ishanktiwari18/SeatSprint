.PHONY: build up down test logs shell

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	docker-compose run --rm backend pytest

shell:
	docker-compose run --rm backend python manage.py shell
