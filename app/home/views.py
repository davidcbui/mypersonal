import os
from flask import (
    current_app,
    render_template,
    request,
    jsonify,
    send_from_directory,
    redirect,
    url_for,
)
from flask_mail import Mail, Message
from . import home
from .forms import UploadForm
from werkzeug.utils import secure_filename

# import webbrowser as wb

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


@home.route("/upload", methods=["GET", "POST"])
def upload():
    title = "Upload File"
    form = UploadForm()
    if form.validate_on_submit():
        f = form.uploadfile.data
        filename = secure_filename(f.filename)

        f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        return redirect("/about")

    return render_template("home/upload.html", title=title, form=form)

