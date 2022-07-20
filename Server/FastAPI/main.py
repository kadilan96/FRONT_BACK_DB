from flask import Flask
from flask_restx import Resource, Api
from rest.userAPI import userApi
from swagger.user import User


app = Flask(__name__)
api = Api(app)

app.register_blueprint(userApi, url_prefix='/user')

api.add_namespace(User, '/user')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
