from flask import Flask, g, jsonify

from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

from auth import auth
import config
import models
from resources.courses import courses_api
from resources.reviews import reviews_api
from resources.users import users_api


app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

limiter = Limiter(app, global_limits=[config.DEFAULT_RATE], key_func=get_ipaddr)
limiter.limit("40/day")(users_api)
limiter.limit(config.DEFAULT_RATE, per_method=True,
              methods=["post", "put", "delete"])(courses_api)
limiter.limit(config.DEFAULT_RATE, per_method=True,
              methods=["post", "put", "delete"])(reviews_api)
#limiter.exempt(courses_api)
#limiter.exempt(reviews_api)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/api/v1/users/token', methods=['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})
  
if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)