import smtplib


HOST = "smtp.night-light54.ru"
TO = "ars.sky@mail.ru" #"nightlight54@mail.ru"
FROM = "admin@night-light54.ru"


def send_mail(subj, text):
    body = u"\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % subj,
        "",
        text
    )).encode('utf-8')

    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], body)
    server.quit()
