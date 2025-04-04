migrate:
	@uv run python manage.py migrate

makemigrations:
	@uv run python manage.py makemigrations

collecstatic:
	@uv run python manage.py collectstatic --no-input

shell:
	@uv run python manage.py shell
