#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

msg = EmailMessage()
msg['Subject'] = "Älteres Öl im Überfluss"
msg['From'] = Address('krother@rubor.de')
msg['To'] = Address("Kristian Academis", "krother@academis.eu")

msg.set_content("Jörg würgt im Sägewerk.")

server = smtplib.SMTP('wp263.webpack.hosteurope.de')
server.login('wp1033735-krother', 'S4tchM00') 
server.send_message(msg)
server.quit()

