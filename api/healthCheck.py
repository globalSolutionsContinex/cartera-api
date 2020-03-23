from flask import Blueprint


def get_health_check_controller():

    health = Blueprint("healthCheck", __name__)

    @health.route("/health_check", methods=["get"])
    def health_check():
        return "ok"

    return health
