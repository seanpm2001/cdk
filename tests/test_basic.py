# -*- coding: utf-8 -*-

import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
    
from .context import cdk

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    
    def test_inserting_custom_css(self):
        """Custom css means opening the produced .html and sneaking
        a style tag before the closing </body> tag."""
        
        source_fp = StringIO('<p>a bunch of</p> html</body>\r\n</html>\r\n')
        css_fp = StringIO('My rules')
        cdk.add_css(source_fp, css_fp)
        source_fp.seek(0)
        out = '<p>a bunch of</p> html<style type="text/css">\r\nMy rules\r\n</style>\r\n</body>\r\n</html>\r\n'
        self.assertEqual(out, source_fp.read())

if __name__ == '__main__':
    unittest.main()
