run:
	docker-compose up -d
down:
	docker-compose down
info:
	docker ps -a

delete-app:
	docker rmi flight
delete-all:
	docker rmi flight && \
	docker rmi postgres:16-alpine && \
	rm -rf db_data

restart:
	docker-compose down && \
	docker rmi flight && \
	docker-compose up -d

run-tests:
	pytest -vs unit_tests/flight.py

# pg_dump -U postgres flight_db > db.sql
