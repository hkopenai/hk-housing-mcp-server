import unittest
from tests.test_tool_private_storage import TestPrivateStorage

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestPrivateStorage))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)
