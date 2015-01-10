#!/usr/bin/env python3

"""
Send a personalized email to a stack of people.
"""

import sys
import re
from send_email import MailAccount
import os

KROTHER_PASSWORD = os.environ['KROTHER_PASSWORD']

class Mail:

    def __init__(self, template, recipient):
        self.template = template
        self.name = recipient[0]
        self.gender = recipient[1]
        self.email = recipient[2]
        self.firstname = self.name.split()[0]

    def apply_template(self):
        mail = self.template
        mail = mail.replace('{{name}}', self.name)
        mail = mail.replace('{{email}}', self.email)
        mail = mail.replace('{{firstname}}', self.firstname)
        if self.gender == 'M':
            mail = re.sub('\{\{F\:[a-zA-Z]*\}\}', '', mail)
            mail = mail.replace('{{M:', '')
            mail = mail.replace('}}', '')
        if self.gender == 'F':
            mail = re.sub('\{\{M\:[a-zA-Z]*\}\}', '', mail)
            mail = mail.replace('{{F:', '')
            mail = mail.replace('}}', '')
        return mail

    def send(self, subject):
        account = MailAccount('wp263.webpack.hosteurope.de', 587, \
                              'wp1033735-krother', KROTHER_PASSWORD, \
                              'krother@rubor.de', "Kristian Rother")
        account.send_email(self.email, subject, self.apply_template())

    def __repr__(self):
        return self.apply_template()


def load_recipients(filename):
    recipients = []
    for line in open(filename):
        tokens = line.strip().split(';;')
        if len(tokens) == 3:
            name, gender, email = tokens
            assert gender in 'MF'
            recipients.append((name, gender, email))
        else:
            print ('WARNING: INVALID LINE\n', line)
    return recipients

def create_mails(template, recipients):
    mails = [Mail(template, r) for r in recipients]
    return mails

def run_mail(template, recipients):
    r = load_recipients(recipients)
    t = open(template).read()
    mails = create_mails(t, r)

    for m in mails:
        print ('-' * 70)
        print ('MAIL TO: ', m.email)
        print ('-' * 70)
        print (m)
        input()

    print ("\nENTER SUBJECT")
    subject = input()
    print ("\nSEND ALL EMAILS? PLEASE CONFIRM BY TYPING 'YES'.")
    x = input()
    if x == 'YES':
       for m in mails:
            m.send(subject)
            print ('MAIL TO %s SENT.' % m.email)


if __name__ == '__main__':
    run_mail(sys.argv[1], sys.argv[2])

