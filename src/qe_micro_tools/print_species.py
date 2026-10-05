from qe_micro_tools.microtool_interface import Microtool
from qe_micro_tools.xml2dict import xml2dict


class PrintSpecies(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

    def implementation(self, args):
        file_name = args.file_name
        data_dict = xml2dict(file_name)
        ans = "ATOMIC_SPECIES\n"
        for item in data_dict['input']['atomic_species']['species']:
            ans += item['@name'] + " " + str(item['mass']) + " " + item['pseudo_file'] + "\n"
        print(ans)
        return ans


def main():
    tool = PrintSpecies()
    tool.entry_point()


if __name__ == "__main__":
    main()

