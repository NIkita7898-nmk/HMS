from app import db,app
from api.model import User,Allocation
from flask import request, jsonify
from flask.views import MethodView
from flask import Blueprint

# user_routes = Blueprint('api', __name__)
class ListView(MethodView):
    def get(self):
        print(self, "********************")
        users = Allocation.query.all()
        print(users, "********************")    
        all_user = []
        for user in users:
            user_dict = {
                "id": user.id,
                "name": f'{user.f_name} {user.l_name}',
                "username": user.username,
                "email": user.email,
                "address": user.address,
                "phone_no": str(user.phone_no)
                }
            all_user.append(user_dict)
        return jsonify({'users': all_user})
    
    def post(self):
        data = request.json
        user_data = User(f_name=data['f_name'], l_name=data['l_name'], username=data['username'], email=data['email'], address=data['address'], phone_no=data['phone_no'])
        db.session.add(user_data)
        db.session.commit()
        return jsonify({'data': user_data})
    
# user_routes.add_url_rule('/getuser', view_func=ListView.as_view('getuser'))
