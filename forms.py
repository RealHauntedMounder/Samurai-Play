from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from config import create_app, bcrypt
from models import *

application = create_app()

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Логин"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Пароль"})

    submit = SubmitField("Зарегистрироваться")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "Пользователь с таким логином уже существует. Пожалуйста, выберите другой логин.")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Логин"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Пароль"})

    submit = SubmitField("Войти")

    def validate_user(self, username, password):
        existing_user = User.query.filter_by(username=username.data).first()
        if not existing_user or not bcrypt.check_password_hash(existing_user.password_hash, password.data):
            raise ValidationError("Неправильный логин или пароль")
