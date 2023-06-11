from flask import render_template, url_for, Blueprint, request, redirect
from pychartjs import BaseChart, ChartType, Color
from forms import Filters, categories, icons, CreateNewOperation
from models import db, Account, User, Transaction
from flask_login import logout_user, login_required, current_user
import os
import webbrowser

class MyBarGraph(BaseChart):

    type = ChartType.Bar

    class data:
        label = "Numbers"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green

signed = Blueprint('signed', __name__, template_folder='signed')
unsigned = Blueprint('unsigned', __name__, template_folder='unsigned')


@unsigned.route('/')
@unsigned.route('/main')
def home():
    return render_template('unsigned/main.html')

backgroundColor= ['#ff6384','#36a2eb','#cc65fe', '#abc234', '#ff6384', '#36a2eb']


@signed.route('/home')
@login_required
def home():
    form = CreateNewOperation()
    print(current_user)
    name = 'Mark'
    surname = 'Tsukerberg'
    return render_template('signed/index.html', data = [3, 7, 1, 6, 13, 27], backgroundColor=backgroundColor, form=form, page='dashboard')


@signed.route('/first')
@login_required
def first():
    return render_template('unsigned/home.html', data = [3, 7, 1, 6, 13, 27], backgroundColor=backgroundColor, form=form, page='dashboard')


@signed.route('/account')
@login_required
def account():
    print(current_user)
    return render_template('signed/account.html', page='account', user=current_user)


@signed.route('/budgets')
@login_required
def budgets():

    items = db.session.query(Account).filter_by(client_id=current_user.id).all()
    print(current_user.id)
    print(items[0].name)
    print(type(items))
    return render_template('signed/budgets.html', page='budgets', items=items)
@signed.route('/operations')
@login_required
def operations():
    form = Filters()
    operations = Transaction.query.filter_by(account=1).all()
    print(operations[1].comment)
    for item in operations:
        if item.comment is None:
            item.comment = ""
    print(operations)
    return render_template('signed/operations.html', page='operations', form=form, categories=categories, icons=icons, operations=operations)


@signed.route('/new_operation')
@login_required
def new_operation():
    return render_template('signed/new_operation.html', page='new_operation')


@signed.route('/connect')
def connect():
    webbrowser.open("http://127.0.0.1:5000/connect/mono")
    return redirect('/account')\

@signed.route('/connect/mono')
def connect_mono():
    return render_template('signed/connect.html')



@signed.route('/log_out')
@login_required
def log_out():
    logout_user()
    return redirect('/')
    return render_template('signed/log_out.html', page='log_out')

