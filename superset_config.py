import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
#ROW_LIMIT = 5000
# For it to work in heroku basic/hobby dynos (increase as you like)
SUPERSET_WORKERS = 1

#SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.environ.get('SECRET_KEY', '\2\1thisismyscretkey\1\2\e\y\y\h')

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:////path/to/superset.db')

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY', '')
