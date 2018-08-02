from flask import render_template, request, jsonify, send_from_directory

from flask_mail import Mail, Message

# from ..email import send_email

# import simplejson as json
from . import home
import webbrowser as wb

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


@home.route("/viewcv")
def get_cv():
    mycv = "resume2018.pdf"
    directory = "static"
    # wb.open_new(mycv)
    return send_from_directory(
        directory=directory, filename=mycv, mimetype="application/pdf"
    )
