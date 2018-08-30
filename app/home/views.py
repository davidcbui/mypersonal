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
from flask_login import login_user, logout_user, login_required, current_user
from . import home
from .forms import UploadForm
from werkzeug.utils import secure_filename

# import webbrowser as wb

mail = Mail()
# favourite links
all_links = [
    {
        "name": "Creating Web API With Flask Python",
        "link": "https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask",
    },
    {
        "name": "Flask with Blueprint",
        "link": "https://www.safaribooksonline.com/library/view/flask-web-development/9781491991725/ch02.html#ch_basic",
    },
    {
        "name": "Guide to Build Better Predictive Models using Segmentation",
        "link": "https://www.analyticsvidhya.com/blog/2016/02/guide-build-predictive-models-segmentation/",
    },
    {
        "name": "Using Python and Auto ARIMA to Forecast Seasonal Time Series",
        "link": "https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c",
    },
    {
        "name": "Cluster & Segmentation Analysis",
        "link": "http://inseaddataanalytics.github.io/INSEADAnalytics/CourseSessions/Sessions45/ClusterAnalysisReading.html",
    },
    {
        'name':'SQLAlchemy CheatSheet',
        'link':'https://www.pythonsheets.com/notes/python-sqlalchemy.html'
    }
]


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
@login_required
def upload():
    title = "Upload File"
    form = UploadForm()
    if form.validate_on_submit():
        f = form.uploadfile.data
        filename = secure_filename(f.filename)

        f.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        return redirect("/about")

    return render_template("home/upload.html", title=title, form=form)


@home.route("/api/v1/resources/links/all", methods=["GET"])
def mylinks():
    return jsonify(all_links)


@home.route("/favorlinks")
def show_favor_links():
    return render_template("home/links.html", links=all_links) #all links predefined on top as list of dictionaries

@home.route("/mylambda")
def consume_myld():
    return render_template("home/alltestgohere.html")    

