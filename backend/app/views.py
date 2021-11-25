from flask import Flask, redirect, request, render_template
from markupsafe import escape
from backend.app.model.message import Message
import os

app = Flask(__name__)
home_page = os.getenv('FRONTEND_URL')


@app.route('/')
def home():
    if home_page:
        return redirect(home_page)
    else:
        return render_template("something_went_wrong.html")


@app.route('/message/save')
def save_message():
    if request != 'POST':
        return home()
    if "message" in request.form:
        message_text = escape(request.form["message"])
        if len(message_text) < 1:
            return render_template("message_is_empty")
        else:
            message = Message(message_text)
            message.save()
    else:
        return render_template("something_went_wrong.html")
