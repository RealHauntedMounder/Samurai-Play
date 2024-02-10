from config import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_owner = db.Column(db.Boolean, default=False)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image_path = db.Column(db.String(255))

    def __str__(self):
        return self.name


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    description = db.Column(db.Text)
    account_details = db.Column(db.Text)
    steam_profile = db.Column(db.String(255))
    price = db.Column(db.Integer)
    purchased = db.Column(db.Boolean, default=False)
    purchase_date = db.Column(db.DateTime)
    game = db.relationship('Game', backref=db.backref('accounts', lazy=True))

    @property
    def game_image_path(self):
        return self.game.image_path
