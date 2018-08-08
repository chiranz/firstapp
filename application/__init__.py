import os

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine
#commented because trying flask_sqlalchemy
#from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
app.config['SECRET_KEY'] = '85e209dcdc4f05a4a9c745641fffc814cb254b21'
# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://rioxhygwbwemti:e7a86e1f6e1691315eb9a00b77105952a3c9756852f310780d00302abd1e1908@ec2-174-129-22-84.compute-1.amazonaws.com:5432/d1s2v7fpgo4ntn"
db = SQLAlchemy(app)
#commented for trying flask_sqlalchemy
#engine = create_engine("postgres://rioxhygwbwemti:e7a86e1f6e1691315eb9a00b77105952a3c9756852f310780d00302abd1e1908@ec2-174-129-22-84.compute-1.amazonaws.com:5432/d1s2v7fpgo4ntn")
#db = scoped_session(sessionmaker(bind=engine))

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
#commented because trying flask_sqlalchemy
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)


#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))
from application import routes