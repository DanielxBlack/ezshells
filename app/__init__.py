#!/usr/bin/env python3


# Import libraries
from flask import Flask


app = Flask(__name__)


# import routes. Putting this at the bottom
# is a workaround to circular imports.
from app import routes
