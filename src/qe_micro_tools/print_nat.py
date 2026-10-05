from microtool_interface import Microtool
from qe_micro_tools.read_xml import get_cell_to_print
from qe_micro_tools.xml2dict import xml2dict


class PrintNAT(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

    def implementation(self, args):
        file_name = args.file_name
        data_dict = xml2dict(file_name)
        ans = str(data_dict['input']['atomic_structure']['@nat'])
        print(ans, end=" ")
        return ans


if __name__ == '__main__':

    tool = PrintNAT()
    tool.entry_point()
