from flask import Flask

def create_app():
   app = Flask(__name__)
   app.secret_key = "mySecretKey"

   #from app import globals
   #globals.initialize()

   #from .regression import regress
   #app.register_blueprint(regress, url_prefix="/reg")

   return app

app = create_app()

from app import views