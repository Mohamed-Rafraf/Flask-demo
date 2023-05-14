import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Flask application
app = Flask(__name__)

# Load the configuration based on the environment
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.Config')

# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

from models import Client

#Index
@app.route("/")
def index():
    return "This is the app index"

#Add client and money
@app.route("/add",methods = ['GET','POST']) #Added by Samuel
def add_client():
    name=request.args.get('name')
    money=request.args.get('money')
    try:
        client=Client(
            name=name,
            money=money
        )
        db.session.add(client)
        db.session.commit()
        return "Client added with id={}".format(client.id)
    except Exception as e:
	    return(str(e))

#Get all clients
@app.route("/getall")
def get_all():
    try:
        clients=Client.query.all()
        return  jsonify([e.serialize() for e in clients])
    except Exception as e:
	    return(str(e))

#Get client by ID
@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        client=Client.query.filter_by(id=id_).first()
        return jsonify(client.serialize())
    except Exception as e:
	    return(str(e))

#Get client by Name
@app.route("/getn/<name_>")
def get_by_name(name_):
    try:
        client=Client.query.filter_by(name=name_).first()
        return jsonify(client.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()
