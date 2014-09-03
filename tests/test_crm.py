import sys
import os 
import re
from unittest import TestCase, main
sys.path.append(os.sep.join(os.getcwd().split(os.sep)[:-1]))
from pyhome.crm import CRM, Contact

TEST_DATA_DIR = os.getcwd() + os.sep + 'test_data' + os.sep
 

class ContactTests(TestCase):

    def setUp(self):
        self.fb = Contact('Fire brigade', 'put out fires', \
                  'fire@hotmail.com', '999', 'www.fi.re', \
                  'good looking', 'guys', 'bla')
    
    def test_empty_attributes(self):
        c = Contact('empty')
        self.assertEqual(c.name, 'empty')
        self.assertEqual(c.tags, [])
        self.assertEqual(c.phone, '')
        self.assertEqual(c.email, '')
        self.assertEqual(c.website, '')

    def test_repr(self):
        s = str(self.fb)
        self.assertEqual(s, 'Fire brigade;;put out fires;;fire@hotmail.com;;999;;www.fi.re;;good looking;;guys;;bla')

    def test_format_text(self):
        s = self.fb.format_text()
        self.assertTrue(re.search('    fire@hotmail.com', s))
        

class CRMTests(TestCase):
    
    def setUp(self):
        self.crm = CRM()
        self.peter = Contact('Peter Pan', 'flying')
        self.minnie = Contact('Minnie Maus', 'mouse')
        self.dumbo = Contact('Dumbo', 'elephant', 'flying')

    def test_init(self):
        self.assertEqual(self.crm.n_contacts, 0)

    def test_add_contact(self):
        self.crm.add_contact(self.peter)
        self.assertEqual(self.crm.n_contacts, 1)

    def test_iterate(self):
        self.crm.add_contact(self.peter)
        self.crm.add_contact(self.minnie)
        result = list(self.crm)
        self.assertEqual(len(result), 2)
        self.assertTrue(self.peter in result)
        self.assertTrue(self.minnie in result)

    def test_get_by_tag(self):
        self.crm.add_contact(self.peter)
        self.crm.add_contact(self.dumbo)
        self.assertEqual(len(self.crm.get_by_tag('flying')), 2)
        self.assertEqual(len(self.crm.get_by_tag('elephant')), 1)
        self.assertEqual(len(self.crm.get_by_tag('mouse')), 0)

    def test_search_text(self):
        crm = CRM()
        crm.load_contacts(open(TEST_DATA_DIR + 'sample_contacts.txt'))
        result = crm.search_text('Marie Curie')
        self.assertEqual(len(result), 2)

    def test_lowercase(self):
        self.crm.add_contact(self.peter)
        result = self.crm.search_text('peter')
        self.assertEqual(len(result), 1)

    def test_load_contacts(self):
        crm = CRM()
        crm.load_contacts(open(TEST_DATA_DIR + 'sample_contacts.txt'))
        self.assertEqual(crm.n_contacts, 11)

    def test_load_tab_fourspace(self):
        crm = CRM()
        crm.load_contacts(['name;;summary;;emil@email.li'])
        self.assertEqual(crm.n_contacts, 1)
        self.assertEqual(crm.contacts[0].email, 'emil@email.li')

    def test_load_striptags(self):
        crm = CRM()
        crm.load_contacts(['name;;summary;;email;;phone number;;tag1;;tag2;;tag3'])
        self.assertTrue('tag2' in crm.contacts[0].tags)
        self.assertFalse('phone' in crm.contacts[0].tags)

    def test_load_fail_notabs(self):
        crm = CRM()
        crm.load_contacts(['this is a line without tabs'])
        self.assertEqual(crm.n_contacts, 0)
        self.assertEqual(len(crm.warnings), 1)

    def test_write_contacts(self):
        self.crm.add_contact(self.peter)
        self.crm.add_contact(self.minnie)
        out = self.crm.write_contacts()
        self.assertEqual(out.count('\n'), 2)
        self.assertTrue('Peter Pan' in out)

    def test_write_load_sanity(self):
        out = self.crm.write_contacts()
        crm = CRM()
        crm.load_contacts(out.split('\n'))
        out2 = self.crm.write_contacts()
        self.assertEqual(out, out2)

 
class CommandLineTests(TestCase):

    def setUp(self):
        os.environ.update({'ACADEMIS_CRM_PATH': TEST_DATA_DIR})
        #self.pathcmd = 'export ACADEMIS_CRM_PATH=%s;'% TEST_DATA_DIR
        #print TEST_DATA_DIR

    def tearDown(self):
        pass
        #if os.path.exists('out.tmp'):
        #    os.remove('out.tmp')
    
    def test_main(self):
        #os.system(self.pathcmd + 'crm Karol > out.tmp')
        os.system('../pyhome/'+'crm Karol > out.tmp')
        out = open('out.tmp').read()
        print 'ALA', out
        self.assertTrue('11 contacts' in out)
        self.assertTrue('Marie Curie' in out)

    def test_warning(self):
        os.system(self.pathcmd + 'crm Karol > out.tmp')
        out = open('out.tmp').read()
        self.assertTrue('INVALID RECORD' in out)


if __name__ == '__main__':
    main()
