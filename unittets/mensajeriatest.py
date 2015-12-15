import unittest

import sys
from os import path
# Recuperamos ruta absoluta del fichero y subimos al directorio principal
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import mensajeria

#import iomensajeria
#import mensajero
#import greedy

class MensajeriaTest(unittest.TestCase):

    def test_file_input_exist_with_data(self):
        print "="*75
        print "Test file exist with data (test_file_input_exist_with_data)"
        print "="*75
        m = mensajeria.Mensajeria(fin='test', fout=False)
        m.init()
        data = m.get_data()
        print "Deberiamos obtener datos"
        print "Test Data: " + str(data) + "\n"
        self.assertIsNotNone(data)
		
    def test_file_input_exist_without_data(self):
        print "="*75
        print "Test file exist without data (test_file_input_exist_without_data)"
        print "="*75
        files = ['test_no_data', 'test_no_data_1', 'test_no_data_2', 'test_no_data_3']
        for f in files:
            m = mensajeria.Mensajeria(fin=f, fout=False)
            m.init()
            data = m.get_data()
            print "Deberiamos objeter data = None"
            print "Test Data: " + str(data) + "\n"
            #self.assertListEqual(data,[])
            self.assertIsNone(data)

    def test_file_input_not_exist(self):
        print "="*75
        print "Test file does not exist (test_file_input_not_exist)"
        print "="*75
        m = mensajeria.Mensajeria(fin='thisfiledoesnotexist', fout=False)
        m.init()
        data = m.get_data()
        print "Deberiamos objeter data = None"
        print "Test Data: " + str(data) + "\n"
        self.assertIsNone(data)

    def test_file_input_wrong_data(self):
        print "="*75
        print "Test file exist with wrong data (test_file_input_wrong_data)"
        print "="*75
        files = ['test_wrong_data', 'test_wrong_data_1', 'test_wrong_data_2', 'test_wrong_data_3']
        for f in files:
            print f
            m = mensajeria.Mensajeria(fin=f, fout=False)
            m.init()
            data = m.get_data()
            print "Deberiamos objeter data = None"
            print "Test Data: " + str(data) + "\n"
            self.assertIsNone(data)
            #self.assertRaises(IOError, lambda: m.init())		
	
if __name__ == '__main__':
    unittest.main()
