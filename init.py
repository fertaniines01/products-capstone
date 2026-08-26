"""
Package: service
Package for the application models and service routes
"""
import os
import sys
import logging
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URI", "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Import the routes After the Flask app is created
from service import routes  # noqa: F401 E402
from service.models import Product, db  # noqa: F401 E402

# Set up logging for production
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    Product.init_db(app)
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

app.logger.info("Service initialized!")
