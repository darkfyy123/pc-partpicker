import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from route_template import template
from route_func import function
from models import GPU, CPU, RAM, MB, CASE, DRIVE, PSU, FAN, BUILD
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Essential for PythonAnywhere to find your DB
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "pcparts.db")

engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(template)
app.register_blueprint(function)


if __name__ == "__main__":
    app.run()
