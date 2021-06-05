from flask import (request, jsonify,
                    url_for, Blueprint,
                    abort)
from .utils import BookReviews
import json 
import os 
current_path = os.path.dirname(os.path.abspath(__file__))
path_config = os.path.join(current_path,"../","../","config.json")
config = open(path_config,"r",encoding="utf-8").read()
config = json.loads(config)

api_views = Blueprint("api_views",__name__,static_folder="static",
                        template_folder="templates")

@api_views.route("/status",methods=["GET"])
def healthy():
    return jsonify({"healthy":True,"status":"OK"})

@api_views.route("/listnames",methods=["GET"])
def listnames():
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    try:
        nyt_resp = bkr.get_list_names()
        resp = {} 
        resp['success'] = True 
        resp['response'] = nyt_resp
        return jsonify(resp)
    except:
        abort(404)

@api_views.route("/lists",methods=["GET"])
def list():
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    if "list" not in request.args:
        abort(404)
    try:
        nyt_resp = bkr.get_list(**request.args)
        resp = {}
        resp['success'] = True 
        resp['response'] = nyt_resp
        return jsonify(resp)
    except:
        abort(404)

@api_views.route("/overview",methods=["GET"])
def overview():
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    try:
        nyt_resp = bkr.get_overview(**request.args)
        resp = {}
        resp['success'] = True 
        resp['response'] = nyt_resp
        return jsonify(resp)
    except:
        abort(404)


@api_views.route("/history",methods=["GET"])
def history():
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    try:
        nyt_response = bkr.best_sellers_history(**request.args)
        resp = {}
        resp['success'] = True 
        resp['response'] = nyt_response
        return jsonify(resp)
    except:
        abort(404)

@api_views.route("/reviews",methods=["GET"])
def reviews():
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    try:
        nyt_response = bkr.get_reviews(**request.args)
        resp = {}
        resp['success'] = True 
        resp['response'] = nyt_response
        return jsonify(resp)
    except:
        abort(404)