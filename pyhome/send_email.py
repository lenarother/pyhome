#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
#from email.message import Message
#from email.MIMEText import MIMEText 
#from email.MIMEBase import MIMEBase 
#from email import encoders


class MailAccount:
    """
    Stores settings for an email account.
    """
    def __init__(self, server,  port, login,  password,  sender_email,  sender_name,  use_tls=False):
        self.server = server
        self.login = login
        self.password = password
        self.sender_email = sender_email
        self.sender_name = sender_name
        self.use_tls = use_tls
        

    def send_email(self, recipient_email, subject, body):
        """Sends an email to a defined address. """
        
        # prepare message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = Address(self.sender_email) #self.sender_name, addr_spec=
        msg['To'] = Address(self.sender_name, recipient_email)

        msg.set_content(body)

        '''
        message = MIMEText(body)
        message["Subject"] = subject 
        message["From"] = self.mail
        message["To"] = recipient_email
        msg = message.as_string()
        '''
        
        server = smtplib.SMTP(self.server)
        
        if self.use_tls: # deliberately starts tls if using TLS
            server.ehlo()
            server.starttls()
            server.ehlo()
            
        server.login(self.login, self.password) 
        server.send_message(msg)
        server.quit()
        return

        
    def send_email_attach(self, recipient_email, subject, body, attachmt, filename):
        """Sends an email to a defined address. """
        # prepare message
        message = MIMEMultipart()
        message["Subject"] = subject 
        message["From"] = self.sender_email
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
