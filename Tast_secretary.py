import unittest
from Secretary import *
from unittest.mock import patch


class Test_sec(unittest.TestCase):

    def test_get_a_name(self):
        self.assertEqual(get_a_name("2207 876234"), "Василий Гупкин")
        self.assertEqual(get_a_name("000 000"), 'Неверный номер')

    def test_get_shelf_number(self):
        self.assertEqual(get_shelf_number('10006'), '2')
        self.assertEqual(get_shelf_number('000 000'), 'Документа под таким номером нет в архиве')

    def test_add_document(self):
        with unittest.mock.patch('builtins.input', return_value='10007'):
            with unittest.mock.patch('builtins.input', return_value='Passport'):
                with unittest.mock.patch('builtins.input', return_value='Сажин Дмитрий'):
                    with unittest.mock.patch('builtins.input', return_value='3'):
                        self.assertEqual(add_document(), None)

    def test_del_document(self):
        self.assertEqual(del_document('11-2'), None)

