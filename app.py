import os
from flask import Flask, Blueprint, url_for


def create_app(test_config=None):
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_mapping(
                SECRET_KEY='somerandomkey',
                #DATABASE=os.path.join(app.instance_path, 'store.sqlite'),
                #SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir, 'store.db'),
                SQLALCHEMY_DATABASE_URI='mysql://root:admin@localhost:3306/store',
            )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from views import bp
    app.register_blueprint(bp)

    @app.route('/')
    def hello_world():  # put application's code here
        return 'Hello World!'


    return app

create_app()
