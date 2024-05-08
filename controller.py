from models import *
from flask import render_template, redirect, url_for, flash, Blueprint, request, jsonify
from flask_admin.contrib.sqla import ModelView
from functools import wraps
from flask_login import login_user, login_required, current_user, logout_user
from config import create_app, bcrypt, babel
from forms import RegisterForm, LoginForm
import requests





routes = Blueprint("routes", __name__, static_folder="static", template_folder="templates")


#@routes.route("/samuraishopadminlogin", methods=['GET', 'POST'])
#    form = LoginForm()
#   if form.validate_on_submit():
#        user = User.query.filter_by(username=form.username.data).first()
#       if user and bcrypt.check_password_hash(user.password_hash, form.password.data) and user.is_owner:
#          login_user(user)
#         return redirect(url_for('routes.admin_panel'))
#    else:
#       flash('Неправильный логин или пароль', 'error')
#
##   return render_template('login.html', form=form)


#@routes.route("/samuraishopadminsignup", methods=['GET', 'POST'])
#def signup():
#    form = RegisterForm()
#
#    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(
#            form.password.data).decode('utf-8')
#        new_user = User(username=form.username.data,
#                        password_hash=hashed_password)
#       db.session.add(new_user)
#       db.session.commit()
#       return redirect(url_for('routes.login'))
#
#   return render_template('register.html', form=form)


#@routes.route('/logout')
#@login_required
#def logout():
#   logout_user()
#    return redirect(url_for('routes.index'))


@routes.route("/")
def index():
    games = Game.query.all()
    return render_template("index.html", games=games)


@routes.route("/game/<int:game_id>")
def game_accounts(game_id):
    game = Game.query.get_or_404(game_id)
    accounts = Account.query.filter_by(game_id=game.id).all()
    return render_template("game_accounts.html", game=game, accounts=accounts)



#class AccountAdminView(ModelView):
    column_list = ['game', 'description', 'steam_profile', 'price']
    form_columns = ['game', 'description', 'account_details',
                    'steam_profile', 'price', 'purchased', 'purchase_date']





#def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_owner:
            return redirect(url_for('routes.index'))
        return f(*args, **kwargs)
    return decorated_function


#@routes.route('/admin')
#@admin_required
#def admin_panel():
#   return redirect(url_for('admin.index'))


@routes.route("/guarantees")
def garantii():
    return render_template("garantii.html")

CREATE_PAYMENT_URL = "https://lk.rukassa.is/api/v1/create"

API_TOKEN = "YOUR_API_TOKEN"

@routes.route('/buy/<int:account_id>')
def buy_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404
    payment_data = {
        'shop_id': 1337,  
        'order_id': account.id,  
        'amount': account.price,  
        'token': API_TOKEN,  
 
    }
    response = requests.post(CREATE_PAYMENT_URL, json=payment_data)
    if response.status_code == 200:
        # Получаем ответ от сервера
        payment_info = response.json()

        payment_url = payment_info.get('payment_url')
        return redirect(payment_url)
    else:
        return jsonify({'error': 'Failed to create payment'}), response.status_code
