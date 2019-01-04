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

TESTFIXTURE = []
for content_type, filename in TESTDATA:
    with open(os.path.join(TESTDATA_DIR, filename)) as f:
        # Remove newline at end of file
        file_content = f.read()[:-1]
        TESTFIXTURE.append((content_type, file_content))


@parameterized_class(('format', 'str'), TESTFIXTURE)
class DeserializeTestCase(unittest.TestCase):
    def test_deserializes_hash_tables(self):
        parsed = SUT.deserialize(self.str, self.format)
        self.assertEqual('10.0.0.1', parsed['servers']['alpha']['ip'])


@parameterized_class(('format', 'str'), TESTFIXTURE)
class SerializeTestCase(unittest.TestCase):
    def setUp(self):
        self.parsed = SUT.deserialize(self.str, self.format)

    def test_serializes_as_original_when_unchanged(self):
        serialized = SUT.serialize(self.parsed, self.format)
        self.assertEqual(self.str, serialized)


if __name__ == '__main__':
    unittest.main()
