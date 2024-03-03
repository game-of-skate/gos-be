start-app:
	docker-compose up

stop-app:
	docker-compose down -v

test-app:
	docker exec gos-be_web_1 bash -c "pytest -svv"