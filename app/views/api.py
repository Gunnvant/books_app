from flask import request, jsonify, render_template, redirect, url_for, Blueprint
import requests
import os

api_views = Blueprint(
    "api_views", __name__, static_folder="static", template_folder="templates"
)
