from microtool_interface import Microtool
from qe_micro_tools.read_xml import get_cell_to_print
from qe_micro_tools.xml2dict import xml2dict


class PrintCell(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

        self.parser.add_argument(
            "--format",
            default="qe",
            choices=["qe", "wan"],
            help=(
                "Output format. "
                "'qe' prints lattice vectors in Quantum ESPRESSO format; "
                "'wan' prints them in Wannier90 format. "
                "(default: %(default)s)"
            ),
        )

    def implementation(self, args):
        file_name = args.file_name
        format = args.format
        data_dict = xml2dict(file_name)
        return get_cell_to_print(data_dict, format=format)


if __name__ == '__main__':

    tool = PrintCell()
    tool.entry_point()
