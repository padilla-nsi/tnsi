import unittest

from unittest.mock import patch # input
from io import StringIO         # output
import sys                      # output

import sandbox as sb

class validation(unittest.TestCase):
    
    # @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=[10, 42])
    def test1(self, mock_in):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            sb.ma_fonction()
            texte = out.getvalue().strip()
            self.assertIn('b 43', texte)
        finally:
            print("tata")
            sys.stdout = saved_stdout
            print("toto")
            print(texte)


        # print(mock_out.getvalue(), file=out)
        # mock_out.assert_called_with('toto')

unittest.main()
