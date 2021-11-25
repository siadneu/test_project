from flask import Flask, redirect, request, render_template
from markupsafe import escape
from model.message import Message
import os

app = Flask(__name__)
home_page = os.getenv('FRONTEND_URL')


@app.route('/')
def home():
    return render_template("something_went_wrong.html", home_url=home_page)


@app.route('/message/save', methods=['GET', 'POST'])
def save_message():
    if request.method != 'POST':
        return home()
    if "message" in request.form:
        message_text = escape(request.form["message"])
        if len(message_text) < 1:
            return render_template("message_is_empty.html", home_url=home_page)
        else:
            message = Message(message_text)
            message.save()
            return render_template("success.html")
    else:
        return render_template("something_went_wrong.html", home_url=home_page)
