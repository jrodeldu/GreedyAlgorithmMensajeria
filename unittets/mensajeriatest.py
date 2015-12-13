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
        print "Test file exist with data"
        m = mensajeria.Mensajeria(fin='test', fout=None)
        data = m.get_data()
        print "Test Data: " + str(data) + "\n"
        self.assertIsNotNone(data)

    def test_file_input_exist_without_data(self):
        print "Test file exist without data"
        m = mensajeria.Mensajeria(fin='test_no_data', fout=None)
        data = m.get_data()
        print "Deberiamos objeter una lista vacia []"
        print "Test Data: " + str(data) + "\n"
        self.assertListEqual(data,[])

    def test_file_input_not_exist(self):
        print "Test file does not exist"
        m = mensajeria.Mensajeria(fin='thisfiledoesnotexist', fout=None)
        data = m.get_data()
        print "Deberiamos obtener None"
        print "Test Data: " + str(data) + "\n"
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
