import smtplib
from email.message import EmailMessage

def send_email(from_email, app_password, to_email, alert_data):
    try:
        msg = EmailMessage()
        msg["Subject"] = "📉 Auto Investment Notifier - Stock Alert"
        msg["From"] = f"Auto Investment Notifier <{from_email}>"
        msg["To"] = to_email

        msg.set_content(
            f"""
Hello,

A discount has been detected for one of your favorite stocks.

Stock: {alert_data['symbol']}
Discount: %{alert_data['discount']}
Current Price: {alert_data['price']}

This email was sent automatically by
Auto Investment Notifier System.
"""
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(from_email, app_password)
            smtp.send_message(msg)

        print("Mail başarıyla gönderildi")

    except Exception as e:
        print("Mail gönderme hatası:", e)
