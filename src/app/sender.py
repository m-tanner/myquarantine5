import requests
from flask import current_app, render_template
from flask_mail import Message


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(
        app.config["MYQ5_MAIL_SUBJECT_PREFIX"] + " " + subject,
        sender=app.config["MYQ5_MAIL_SENDER"],
        recipients=[to],
    )
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    request = requests.post(
        "https://us-central1-four-track-friday-2.cloudfunctions.net/mq5_send_email",
        data={"Body": msg.html, "To": msg.recipients[0], "Subject": msg.subject},
    )
    print(request.text)
