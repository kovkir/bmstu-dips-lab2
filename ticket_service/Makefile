run:
	docker-compose up -d
down:
	docker-compose down
info:
	docker ps -a

delete-app:
	docker rmi ticket
delete-all:
	docker rmi ticket && \
	docker rmi postgres:16-alpine && \
	rm -rf db_data

restart:
	docker-compose down && \
	docker rmi ticket && \
	docker-compose up -d

run-tests:
	pytest -vs unit_tests/ticket.py

# pg_dump -U postgres ticket_db > db.sql
