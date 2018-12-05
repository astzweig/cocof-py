#!/usr/bin/env python
import unittest
import os
import cocof.filehandling as SUT
from parameterized.parameterized import parameterized_class
TESTDATA_DIR = os.path.dirname(__file__)
TESTDATA = [
    ('toml', 'test.toml'),
    ('yaml', 'test.yml'),
    ('json', 'test.json')
]

TESTFIXTURE=[]
for content_type, filename in TESTDATA:
    with open(os.path.join(TESTDATA_DIR, filename)) as f:
        file_content = f.read()
        TESTFIXTURE.append((content_type, file_content))


@parameterized_class(('format', 'str'), TESTFIXTURE)
class ReadFileTestCase(unittest.TestCase):
    def test_parse_content(self):
        parsed = SUT.parse_content(self.str, self.format)
        self.assertEqual('10.0.0.1', parsed['servers']['alpha']['ip'])


if __name__ == '__main__':
    unittest.main()
