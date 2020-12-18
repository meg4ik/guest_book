#python app.py --settings=common
import secrets

secret_key = secrets.token_hex(16)

DEBUG=True
WTF_CSRF_ENABLED=False
SECRET_KEY=secret_key

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:totalmag@localhost/guest_book'
SQLALCHEMY_TRACK_MODIFICATIONS = False