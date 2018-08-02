from flask import render_template, request, jsonify

from flask_mail import Mail, Message

# from ..email import send_email

# import simplejson as json
from . import home

mail = Mail()


@home.route("/about")
def about_me():
    title = "David Bui Resume"
    return render_template("home/index.html", title=title)


@home.route("/contact", methods=["POST"])
def contact_form():

    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    # how about sending email and returns json response to view

    msg = Message(subject, sender=email, recipients=["dbui@tiksol.com"])
    msg.body = message
    mail.send(msg)

    return jsonify(
        success=1, status="OK", name=name, email=email, subject=subject, message=message
    )
