db-migrate:
	@echo "Running migrations"
	@echo "-" * 20
	python -m src.scripts.run_migrations
	@echo "-" * 20
	@echo "Migration execution finished"


app-build:
	docker-compose build --no-cache

app-up:
	docker-compose --env-file .env up -d