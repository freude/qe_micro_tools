from qe_micro_tools.microtool_interface import Microtool
from qe_micro_tools.xml2dict import xml2dict


class PrintNTYP(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

    def implementation(self, args):
        file_name = args.file_name
        data_dict = xml2dict(file_name)
        ans = len(data_dict['input']['atomic_species']['species'])
        print(ans, end=" ")
        return ans


def main():
    tool = PrintNTYP()
    tool.entry_point()


if __name__ == "__main__":
    main()
