from flask import render_template, Blueprint


bp = Blueprint('free', __name__, template_folder='bp')

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('bp/home.html')

@bp.route('/first')
def first():
    return render_template('bp/first.html')

