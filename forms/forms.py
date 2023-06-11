""" The form  file """
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from markupsafe import Markup

categories = ['Transport', 'Hygiene', 'Additional', 'Housing', 'Communications', 'Health', 'Cafes', 'Car', 'Clothes',
             'Gifts', 'Bills', 'Entertainment', 'Sports', 'Taxi', 'Transport', 'Pets']
icons = [Markup("<i class='bx bx-basket' ></i>"), Markup("<i class='bx bx-shower'></i>"),
         Markup("<i class='bx bx-coin' ></i>"), Markup("<i class='bx bx-building-house' ></i>"),
         Markup("<i class='bx bx-phone' ></i>"), Markup("<i class='bx bx-heart'></i>"),
         Markup("<i class='bx bx-restaurant'></i>"), Markup("<i class='bx bx-car' ></i>"),
         Markup("<i class='bx bx-closet'></i>"), Markup("<i class='bx bx-gift' ></i>"),
         Markup("<i class='bx bx-receipt'></i>"), Markup("<i class='bx bx-happy-alt'></i>"),
         Markup("<i class='bx bx-basketball' ></i>"), Markup("<i class='bx bx-taxi' ></i>"),
         Markup("<i class='bx bx-train' ></i>' ></i>"), Markup("<i class='bx bx-bone'></i>")]
Categories = categories
print('1:',Categories)
Categories.insert(0, '----')
print('2:',Categories)
year=date.today()
class CreateClientForm(FlaskForm):
    """ The client form """
    first_name  = StringField("First name", validators=[DataRequired(), Length(min=1, max=40)])
    last_name   = StringField("Last name", validators=[DataRequired(), Length(min=1, max=40)])
    #email       = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=80)])
    phone       = StringField("Phone", validators=[DataRequired(), Length(min=13, max=13)])
    cancel = SubmitField("Cancel")
    submit = SubmitField("Save")

class CreateNewOperation(FlaskForm):
    myChoices = ['----','Mono', 'PUMB', 'Privat'] # number of choices
    category = SelectField("Wallet" ,choices=myChoices, validators=[DataRequired()])

class CreateOrderForm(FlaskForm):
    """ The order form """
    name        = StringField("Full name", validators=[DataRequired(), Length(min=6, max=80)])
    phone       = StringField("Phone", validators=[DataRequired(), Length(min=13, max=13)])
    order       = StringField("Order", validators=[DataRequired(), Length(min=5, max=200)])
    address     = StringField("Address", validators=[DataRequired(), Length(min=5, max=160)])
    date        = DateField("Date", validators=[DataRequired()])
    cancel = SubmitField("Cancel")
    submit = SubmitField("Save")


class CreateProductForm(FlaskForm):
    """ The product form """
    name        = StringField("Product name",\
                    validators=[DataRequired(), Length(min=6, max=40)])
    cost       = IntegerField("Price",\
                    validators=[DataRequired(), NumberRange(min=1, max=100000)])
    category    = StringField("Category",\
                    validators=[DataRequired(), Length(min=2, max=20)])
    year        = IntegerField("Year",\
                    validators=[DataRequired(), NumberRange(min=2000, max=2023)])
    amount      = IntegerField("Amount",\
                    validators=[DataRequired(), NumberRange(min=1, max=100000)])
    cancel = SubmitField("Cancel")
    submit = SubmitField("Save")


class Filters(FlaskForm):
    """ The filters form """
    date_from   = DateField("from:", validators=[DataRequired()])
    date_to     = DateField("to:", validators=[DataRequired()])
    price_from  = IntegerField("from:",  validators=[DataRequired()])
    price_to    = IntegerField("to:",  validators=[DataRequired()])
    category    = SelectField("category", choices=Categories)
    type        = SelectField("type", choices=['----','income', 'outcome'])
    refresh     = SubmitField("Filter")


class DeleteItem(FlaskForm):
    """ The dalete form """
    cancel = SubmitField("No")
    submit = SubmitField("Yes")
