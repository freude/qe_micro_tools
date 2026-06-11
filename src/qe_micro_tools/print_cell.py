import argparse
from xml2dict import xml2dict
from read_xml import get_cell_to_print


def main():
    parser = argparse.ArgumentParser(
        description=("Extract and print unit-cell lattice vectors"
                     "from a Quantum ESPRESSO XML output file."
                     )
    )

    parser.add_argument(
        "file_name",
        metavar="XML_FILE",
        help="Path to the Quantum ESPRESSO XML file."
    )

    parser.add_argument(
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

    parser.add_argument("--save", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    data_dict = xml2dict(args.file_name)
    result = get_cell_to_print(data_dict, format=args.format)
    print(result)

    if args.save:
        file_path = "cell.out"
        try:
            # Open the file in 'w' (write) mode
            with open(file_path, 'w') as text_file:
                text_file.write(result)
            print(f"Successfully wrote string to {file_path}")
        except IOError as e:
            print(f"Error writing to file: {e}")


if __name__ == '__main__':
    main()
