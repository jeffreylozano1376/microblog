from flask import Flask
from config import Config

# creates an instance of class Flask
app = Flask(__name__) # parameter sets-up as main file for loading resources
app.config.from_object(Config)

from app import routes