import os

from flask import Flask
from flask import request
BASE_URL = 'http://yabitly/'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)



    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import generateUrl
    generateUrl.init_app(app)
    # a simple page that says hello
    @app.route('/generateUrl')
    def generateURL():
        url = request.args.get('url')
        if url is None or len(url.strip()) == 0:
            return  'Invalid Url : Please send proper URL', 400 

        newUrl = BASE_URL + generateUrl.generateUrl(url)
        return newUrl

    # a simple page that says hello
    @app.route('/redirect')
    def redirect():
        redirectUrl = None
        return 'redirect To : {}'.format(redirectUrl)

    return app