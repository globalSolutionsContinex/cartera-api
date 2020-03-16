from flask import Blueprint, Response, request
import api.client.service as service
import json


def get_client_controller(config):

    client_b = Blueprint("client", __name__)
    client_service = service.Client(config)

    @client_b.route("/list/<int:year>", methods=["get"])
    def get_clients(year):
        return send_response("success", "get_clients", client_service.get_list, year=year)

    @client_b.route("/", methods=["post", "put"])
    def create_client():
        if request.method == 'PUT':
            return send_response("Creación exitosa", "create_client", client_service.create, request=request)
        if request.method == 'POST':
            return send_response("Actualización exitosa", "create_client", client_service.update, request=request)

    def send_error(error_msg, func_name, data):
        error = {"error": f"{func_name} error: {str(error_msg)}", "data": data}, 400
        print(error)
        return error

    def send_response(success_message, func_name, func, **args):
        try:
            data = func(**args)
            return Response(json.dumps({"data": data, "message": success_message}), mimetype='application/json')
        except Exception as ex:
            return send_error(ex, func_name, [])

    return client_b

