from flask import Flask

app = Flask(__name__)

from . import app  # Это важно для правильного импорта