"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import PythonFlaskApi.user
import utility.appconfig
import utility.constant
