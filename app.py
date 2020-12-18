from flask import Flask, request, render_template, url_for
from simple_settings import settings
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import MultiDict
import os

app = Flask(__name__, template_folder= os.path.dirname(__file__))
try:
    app.config.update(**settings.as_dict())
except:
    print ("Please configurate your environment!")

db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def main_fu():
    return render_template("main.html"), 200

@app.route("/comment", methods=["POST"])
def Comment_fu():
    from models import Comment
    from forms import CommentForm
    form = CommentForm(request.form)
    print(request.form)
    if form.validate():
        commentsql = Comment(**form.data)
        db.session.add(commentsql)
        db.session.commit()
        return "lol", 200
    else:
        return "lol1", 400

        
if __name__ == "__main__":
    from models import *
    db.create_all()
    app.run()