import os
import unittest
from unittest.mock import patch
import io
from qe_micro_tools import print_cell
from qe_micro_tools import print_coords

coords = """ATOMIC_POSITIONS angstrom
B 0.0 0.0968987085 0.0
N -1.4207e-06 1.5436932968999997 0.0"""

cell = """CELL_PARAMETERS angstrom
 2.5057875667  0.0000000000  0.0000000000
-1.2528937834  2.1702126385  0.0000000000
 0.0000000000  0.0000000000  12.3156439232"""

print(coords)
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data/data-file-schema.xml")

class TestMyCLI(unittest.TestCase):

    # # Strategy A: Directly testing the core business logic unit
    # def test_core_logic(self):
    #     result = my_cli.process_data("hello", uppercase=True)
    #     self.assertEqual(result, "HELLO")

    @patch('sys.argv', ['print_cell', file_path])
    def test_cli_parsing_with_patch(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            print_cell.main()
            self.assertEqual(fake_out.getvalue().strip(), cell)


if __name__ == '__main__':
    unittest.main()
