pip-install:
	pip install -r requirements.lock

pip-upgrade:
	pip install -r requirements.unlocked.txt --upgrade
	pip freeze > requirements.lock

setup:
	fabmanager create-admin --app superset
	superset db upgrade
	superset init

run:
	superset runserver
