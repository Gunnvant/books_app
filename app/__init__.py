from flask import Flask, abort, jsonify 
from .views.api import api_views

def create_app(*args, **kwargs):
    app = Flask(__name__)
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,PATCH,DELETE,OPTIONS"
        )
        return response
    
    app.register_blueprint(api_views,url_prefix="/apiv3")

    @app.errorhandler(404)
    def not_found(error):
        message = {
            "success": False,
            "error": 404,
            "message": "resource not found"}
        return jsonify(message), 404

    @app.errorhandler(422)
    def unprocessable(error):
        message = {
            "success": False,
            "error": 422,
            "message": "unprocessable entity"}
        return jsonify(message), 422

    @app.errorhandler(405)
    def not_allowed(error):
        message = {
            "success": False,
            "error": 405,
            "message": "method not allowed"}
        return jsonify(message), 405

    @app.errorhandler(400)
    def bad_request(error):
        message = {"success": False, "error": 400, "message": "bad request"}
        return jsonify(message), 400

    @app.errorhandler(401)
    def unauthorized(error):
        message = {"success": False, "error": 401, "message": "unauthorized"}
        return jsonify(message), 401
    
    @app.errorhandler(500)
    def server_error(error):
        message = {"succes":False,"error":500, "message":"server error"}
        return jsonify(message), 500
    return app
