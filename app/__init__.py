from flask import Flask

my_app = Flask(__name__)
my_app.debug = True
my_app.secret_key = 'edowaconan'
from app import views