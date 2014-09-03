
import smtplib
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email import encoders

class MailAccount:
    """
    Stores settings for an email account.
    """
    def __init__(self, server,  port, login,  password,  sender_email,  sender_name,  use_tls=False):
        self.server = server
        #TODO: port
        self.login = login
        self.password = password
        self.mail = sender_email
        self.sender = '"%s" <%s>'%(sender_name, sender_email)
        self.use_tls = use_tls
        

    def send_email(self, recipient_email, subject, body):
        """Sends an email to a defined address. """
        # prepare message
        message = MIMEText(body)
        message["Subject"] = subject 
        message["From"] = self.mail
        message["To"] = recipient_email
        msg = message.as_string()

        server = smtplib.SMTP(self.server)
        server.set_debuglevel(1)
 
        if self.use_tls: # deliberately starts tls if using TLS
            server.ehlo()
            server.starttls()
            server.ehlo()
            
        server.login(self.login, self.password) 
        server.sendmail(self.mail, recipient_email, msg)
        server.quit()


    def send_email_attach(self, recipient_email, subject, body, attachmt, filename):
        """Sends an email to a defined address. """
        # prepare message
        message = MIMEMultipart()
        message["Subject"] = subject 
        message["From"] = self.mail
        message["To"] = recipient_email
        message.preamble = body

        # text
        msg = MIMEText(body)
        msg.add_header('text', 'plain')
        message.attach(msg)

        # attachment
        fb = open(attachmt, 'rb')
        msg = MIMEBase('application', 'pdf')
        msg.set_payload(fb.read())
        fb.close()
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)

        composed = message.as_string()

        server = smtplib.SMTP(self.server)
        server.set_debuglevel(1)
 
        if self.use_tls: # deliberately starts tls if using TLS
            server.ehlo()
            server.starttls()
            server.ehlo()
            
        server.login(self.login, self.password) 
        server.sendmail(self.mail, recipient_email, composed)
        server.quit()
