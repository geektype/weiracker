import unittest
import models


class TestData(unittest.TestCase):
    def setUp(self):
        self._data_file = models.Data(filename='test_data.csv')

    def test_read_and_line_count(self):
        data, lines = self._data_file._read()
        self.assertEqual(lines, 1)
        self.assertEqual(data, [{'date': '2020-07-23', 'pull': '37', 'push': '39', 'weight': '71.65'}])  # noqa: E501

    def test_read_header(self):
        result = self._data_file._read_header()
        self.assertEqual(result, ['date', 'push', 'pull', 'weight'])
