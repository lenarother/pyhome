
import sys
import os
import warnings
import re

SEPARATOR = ';;'

class Contact:
    
    def __init__(self, *args):
        self.data = args

    @property
    def name(self):
        return self.data[0]

    @property
    def tags(self):
        return list(self.data[1:])

    @property
    def phone(self):
        for d in self.data:
            if re.search('[\d\s+-]+\Z', d):
                return d
        return ''

    @property
    def email(self):
        for d in self.data:
            if '@' in d:
                return d
        return ''

    @property
    def website(self):
        for d in self.data:
            if d.startswith('http://') or d.startswith('www.'):
                return d
        return ''

    def contains(self, text):
        text = text.lower()
        data = ''.join(map(str, self.data)).lower()
        if text in data:
            return True

    def format_text(self):
        result = self.name + '\n'
        for d in self.data[1:]:
            result += '    ' + d + '\n'
        return result[:-1]
        result += '%-15s\t%s\n' % ('name', self.name)
        if self.tags: result += '%-15s\t%s\n' % ('tags', ', '.join(self.tags))
        if self.email: result += '%-15s\t%s\n' % ('email', self.email)
        if self.phone: result += '%-15s\t%s\n' % ('phone', self.phone)
        if self.website: result += '%-15s\t%s\n' % ('website', self.website)
        if self.summary: result += '%-15s\t%s\n' % ('summary', self.summary)
        if self.notes: result += '%-15s\t%s\n' % ('notes', self.notes)
        return result[:-1]

    def __repr__(self):
        return SEPARATOR.join(self.data)


class CRM:

    def __init__(self):
        self.contacts = []
        self.warnings = []

    @property
    def n_contacts(self):
        return len(self.contacts)

    def add_contact(self, contact):
        self.contacts.append(contact)

    def load_contacts(self, lines):
        for i, line in enumerate(lines):
            line = line.replace('    ', SEPARATOR)
            line = line.replace('\t', SEPARATOR)
            col = line.strip().split(SEPARATOR)
            if len(col) > 1:
                self.add_contact(Contact(*col))
            elif col:
                self.warnings.append('INVALID RECORD IN LINE %i: %s' % (i+1, line))

    def write_contacts(self):
        result = ''
        for contact in self:
            result += str(contact) + '\n'
        return result

    def __iter__(self):
        return iter(self.contacts)

    def get_by_tag(self, tag):
        return [c for c in self.contacts if tag in c.tags]

    def search_text(self, text):
        return [c for c in self.contacts if c.contains(text)]


def run_crm(argv):
    if len(argv) != 1:
        print ('usage crm <search term>')
    else:
        term = argv[0]
        path = os.environ.get('CRM_PATH', '')
        crm = CRM()
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(path + filename) as f:
                    crm.load_contacts(f)
        print ('%i contacts loaded' % crm.n_contacts)
        print ('-' * 79)
        if crm.warnings:
            for warning in crm.warnings:
                print (warning)
            print ('-' * 79)
        for contact in crm.search_text(term):
            print (contact.format_text())
            print ('-' * 79)


if __name__ == '__main__':
    run_crm(sys.argv)

