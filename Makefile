# Get ip for android and ios emulators. Put in .env.local of GameOfSkate project
get-ip:
	ipconfig getifaddr en0

start-docker:
	docker compose up --build

run-docker:
	docker compose up --no-build

stop-docker:
	docker-compose down -v

run-server:
	source venv/bin/activate && python src/manage.py runserver 0.0.0.0:8000

test:
	docker exec gos-be_web_1 bash -c "pytest -svv"

