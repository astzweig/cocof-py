#!/usr/bin/env python
import unittest
import os
import cocof.filehandling as SUT
from parameterized.parameterized import parameterized_class
TESTDATA_DIR = os.path.dirname(__file__)
TESTDATA = [
    ('toml', 'test.toml'),
    ('yaml', 'test.yml'),
    ('json', 'test.json'),
    ('plist', 'de.astzweig.test.plist'),
    ('plist_binary', 'de.astzweig.test.binary.plist')
]

TESTFIXTURE = []
for content_type, filename in TESTDATA:
    with open(os.path.join(TESTDATA_DIR, filename), 'rb') as f:
        # Remove newline at end of file
        file_content = f.read().rstrip(os.linesep.encode('utf-8'))
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
        if self.format == 'plist_binary':
            # Nothing to test for binary format
            return

        serialized = SUT.serialize(self.parsed, self.format)
        if not isinstance(serialized, bytes):
            serialized = serialized.encode('utf-8')
        self.assertEqual(self.str, serialized)


if __name__ == '__main__':
    unittest.main()
