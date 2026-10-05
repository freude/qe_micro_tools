from qe_micro_tools.microtool_interface import Microtool
from qe_micro_tools.read_xml import get_coords_to_print
from qe_micro_tools.xml2dict import xml2dict


class PrintCoords(Microtool):

    def __init__(self):

        description = ("Extract and print atomic coordinates"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

        self.parser.add_argument(
            "--format",
            default="qe",
            choices=["qe", "wan"],
            help=(
                "Output format. "
                "'qe' prints coordinates in Quantum ESPRESSO format; "
                "'wan' prints them in Wannier90 format. "
                "(default: %(default)s)"
            ),
        )

    def implementation(self, args):
        file_name = args.file_name
        format = args.format
        data_dict = xml2dict(file_name)
        ans = get_coords_to_print(data_dict, format=format)
        print(ans)
        return ans


def main():
    tool = PrintCoords()
    tool.entry_point()


if __name__ == "__main__":
    main()
