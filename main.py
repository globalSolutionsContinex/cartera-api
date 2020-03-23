from flask import Flask
from flask_cors import CORS
from api.client import controller as client
from api import healthCheck as health
from infrastructure import config
import infrastructure.log as log

logger = log.get_logger("Main")

app_name = "cartera"
prefix = f'/api/{app_name}'
app = Flask(__name__)
cors = CORS(app)

configData = config.Config()

health_check_controller = health.get_health_check_controller()
client_controller = client.get_client_controller(configData)

app.register_blueprint(health_check_controller, url_prefix=f'{prefix}')
app.register_blueprint(client_controller, url_prefix=f'{prefix}/client')

if __name__ == "__main__":
    logger.info("--------------- Init Cartera Api -------------")
    app.run(port=80)
