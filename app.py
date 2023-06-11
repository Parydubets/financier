import os
from flask_migrate import Migrate
from models import db, User
from flask import Flask, Blueprint, url_for, redirect, jsonify, flash, render_template
from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import json


def create_app(test_config=None):
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_user = os.environ.get('DB_USER')
    db_user = str(db_user) + ':'
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    app.config.from_mapping(
                SECRET_KEY='somerandomkey',
                #DATABASE=os.path.join(app.instance_path, 'store.sqlite'),
                #SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir, 'store.db'),
                SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:admin@localhost:3306/store',
            )
    oauth = OAuth(app)

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

    from views import signed, unsigned
    app.register_blueprint(signed)
    app.register_blueprint(unsigned)
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    ###test
    # blueprint for auth routes in our app

    ###test


    @login_manager.user_loader
    def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        print('getting user', User.query.get(id), id)
        return User.query.get(id)

    migrate = Migrate(app, db, directory='dyplom/migrations')

    @app.cli.command('seed')
    def seed():
        with app.app_context():
            user1 = User(email="peter@gmail.com", name="Peter Parker", given_name="Peter",
                             family_name="Parker")

            db.session.add(user1)
            db.session.commit()
            return "Seeded successfully"


    @app.route('/google')
    def google():
        try:
            GOOGLE_CLIENT_ID = '931862257753-5vsrr6mmq4surnc9a5jv1dlsmdd7hb6a.apps.googleusercontent.com'
            GOOGLE_CLIENT_SECRET = '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'

            CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
            oauth.register(
                name='google',
                client_id=GOOGLE_CLIENT_ID,
                client_secret=GOOGLE_CLIENT_SECRET,
                server_metadata_url=CONF_URL,
                client_kwargs={
                    'scope': 'openid email profile'
                }
            )

            # redirect to google_auth function
            redirect_uri = url_for('google_auth', _external=True)
            print(redirect_uri)
            return oauth.google.authorize_redirect(redirect_uri)
        except:
            flash("An error occured")
            return render_template('/')



    @app.route('/google/auth')
    def google_auth():
        token = oauth.google.authorize_access_token()
        user_info = token['userinfo']
        exists = User.query.filter_by(email=user_info['email']).first()
        try:
            family_name=user_info['family_name']
        except:
            family_name=''
        try:
            given_name=user_info['given_name']
        except:
            given_name=''
        user = User(name=user_info['name'], given_name=given_name,
                    family_name=family_name,
                    email=user_info['email'])
        print(exists)

        if exists is None:

            db.session.add(user)
            db.session.commit()
        print(user_info)
        user= User.query.filter_by(email=user_info['email']).first()
        print("User info", user_info['name'])

        print("          ", user_info['locale'])
        print("          ", user_info['email'])
        login_user(user)
        print("USER", exists.name, exists.email, exists.id)
        print(current_user.name)
        print(current_user)

        # user = oauth.google.parse_id_token(token)
        #print(token)
        return redirect('/home')


    @app.route('/zxc')
    @login_required
    def zxc():
        print(current_user)
        return "HALO"

    return app



create_app()

"""user = jsonify(token)
        user = token.json()
        print("User", user)
        json_object = json.loads(user)

        json_formatted_str = json.dumps(json_object, indent=2)

        print(json_formatted_str)"""