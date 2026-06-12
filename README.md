# qe_micro_tools

<!--
[![PyPI - Version](https://img.shields.io/pypi/v/qe-micro-tools.svg)](https://pypi.org/project/qe-micro-tools)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qe-micro-tools.svg)](https://pypi.org/project/qe-micro-tools)
-->

------------------------------------------------------------------------

This project offers a collection of utilities for parsing and processing
Quantum ESPRESSO output files and for preparing input files for Quantum
ESPRESSO, BerkeleyGW (BGW), and Wannier90 workflows.

## Installation

``` console
pip install .
```

## Usage

The tools provided by `qe-micro-tools` can be used to extract structural
information from Quantum ESPRESSO XML output files
(`data-file-schema.xml`).

For example the tool `print_cell` with the file specified:

``` console
print_cell data-file-schema.xml
```

prints the unit cell vectors:

``` text
CELL_PARAMETERS angstrom
     2.4653562700     -0.0000000000      0.0000000000
    -1.2326781350      2.1350657027      0.0000000000
     0.0000000000      0.0000000000     20.0000000000
```

The atomic coordinates can be extracted using:

``` console
print_coords data-file-schema.xml
```

which prints:

``` text
ATOMIC_POSITIONS angstrom
C      0.0000000000     -0.0000150866      8.2501247404
C      1.2326781350      0.7116419763      8.2507044623
C      1.2326781350      0.7116058553     11.7492947302
C      0.0000000000      1.4232392491     11.7498760670
```

The utilities read the Quantum ESPRESSO XML file directly and print the
extracted information in a format compatible with common Quantum
ESPRESSO input/output conventions.

## Command-line options

Both `print_cell` and `print_coords` are command line tools with the following parameters:

### `print_cell`

``` console
print_cell --help
```

Output:

``` text
usage: print_cell [-h] [--format {qe,wan}] [--save | --no-save] XML_FILE

Extract and print unit-cell lattice vectors from a Quantum ESPRESSO XML output file.

positional arguments:
  XML_FILE           Path to the Quantum ESPRESSO XML file.

options:
  -h, --help         show this help message and exit
  --format {qe,wan}  Output format. 'qe' prints lattice vectors in Quantum ESPRESSO format; 'wan' prints them in Wannier90 format. (default: qe)
  --save, --no-save  Save output to file or print to stdout.
```

### `print_coords`

``` console
print_coords --help
```

Output:

``` text
usage: print_coords [-h] [--format {qe,wan}] [--save | --no-save] XML_FILE

Extract and print atomic coordinates from a Quantum ESPRESSO XML output file.

positional arguments:
  XML_FILE           Path to the Quantum ESPRESSO XML file.

options:
  -h, --help         show this help message and exit
  --format {qe,wan}  Output format. 'qe' prints coordinates in Quantum ESPRESSO format; 'wan' prints them in Wannier90 format. (default: qe)
  --save, --no-save  Save output to file or print to stdout.
```

## License

`qe-micro-tools` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.

