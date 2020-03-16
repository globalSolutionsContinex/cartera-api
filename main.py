from flask import Flask
from flask_cors import CORS
from api.client import controller as client
from infrastructure import config

app_name = "cartera"

app = Flask(__name__)
cors = CORS(app)

configData = config.Config()

client_controller = client.get_client_controller(configData)

app.register_blueprint(client_controller, url_prefix=f'/api/{app_name}/client')

if __name__ == "__main__":
    app.run()
