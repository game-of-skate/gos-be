start-docker:
	brew services stop postgresql # stop postgres if it's running
	&& docker-compose build --no-cache

run-docker:
	docker-compose up

stop-docker:
	docker-compose down -v

test:
	docker exec gos-be_web_1 bash -c "pytest -svv"

