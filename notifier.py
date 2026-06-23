import smtplib
from email.mime.text import MIMEText
from datetime import datetime

from constants import EMAIL_SENDER, EMAIL_RECEIVERS, EMAIL_PASSWORD


def send_email(subject, message):
    print(f"[{datetime.now()}] Sending email...")

    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECEIVERS)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)

            server.sendmail(
                EMAIL_SENDER,
                EMAIL_RECEIVERS,
                msg.as_string()
            )

        print("Email sent successfully!")

    except Exception as e:
        print("Email error:", e)