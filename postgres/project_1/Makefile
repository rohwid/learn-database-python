clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

# Fill database
init:
	python manage.py init

# Migrate if there are an upgrade for database
migrate:
	python manage.py db migrate

# Implement the latest db migrate
upgrade:
	python manage.py db upgrade

# Roll back to the previous db migrate
downgrade:
	python manage.py db downgrade

#
run:
	python manage.py run	

run-prod:
	gunicorn -b 0.0.0.0:5000 manage:app