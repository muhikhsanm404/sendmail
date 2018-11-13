import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = “muhikhsanm2018@gmail.com”
toaddr = “cahyoajiasmoro@gmail.com”
msg = MIMEMultipart()
msg[‘From’] = fromaddr
msg[‘To’] = toaddr
msg[‘Subject’] = “Hai apa kabar !”

body = “Baik”
msg.attach(MIMEText(body, ‘plain’))

server = smtplib.SMTP(‘smtp.gmail.com’, 587)
server.starttls()
server.login(fromaddr, “password pengirim”)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

