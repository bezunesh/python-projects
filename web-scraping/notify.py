import smtplib

sender = "zueb21@gmail.com"
receiver = "bezunesh.terkik@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("97d022cd946b62", "35eff720fc6223")
    server.sendmail(sender, receiver, message)