run:
	docker-compose up -d
down:
	docker-compose down
info:
	docker ps -a

delete-all:
	docker rmi flight_service; \
	docker rmi ticket_service; \
	rm -rf db_data_flight; \
	rm -rf db_data_ticket;

restart:
	docker-compose down && \
	docker rmi flight_service && \
	docker rmi ticket_service && \
	docker-compose up -d

# run-tests:
# 	pytest -vs unit_tests/flight.py

# pg_dump -U postgres flight_db > db.sql