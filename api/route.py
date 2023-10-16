from flask import Blueprint
from api.views import ListView
from api.model import User
routes = Blueprint(User, __name__)
routes.add_url_rule('/getuser', view_func=ListView.as_view('getuser'))
