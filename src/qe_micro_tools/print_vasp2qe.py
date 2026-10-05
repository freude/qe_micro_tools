import os
import io
from ase.io import read
from ase.io.espresso import write_espresso_in
from ase.visualize import view
from microtool_interface import Microtool
from qe_micro_tools.read_xml import get_cell_to_print


class PrintVASP2QE(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

    def implementation(self, args):

        label = "ab_bilayer_relax"

        control = {"calculation": 'vc-relax',
                   "outdir": 'tmp_' + label,
                   "prefix": label,
                   "forc_conv_thr": 1e-05
                   }

        system = {"ecutwfc": 80,
                  "input_dft": 'pbe',
                  "assume_isolated": '2D',
                  "vdw_corr": 'grimme-d3',
                  "occupations": 'smearing',
                  "degauss": 0.02,
                  "smearing": 'mv',
                  "ntyp": 1,
                  "nat": 8,
                  "ibrav": 0
                  }

        ions = {"ion_dynamics": 'bfgs', }

        cell = {"cell_dynamics": 'bfgs',
                "cell_dofree": '2Dxy'}

        electrons = {"conv_thr": 5e-07}

        input_data = {"control": control, "system": system, "electrons": electrons, "ions": ions, "cell": cell}

        dirname = args.file_name
        atoms = read(os.path.join(dirname, "POSCAR"))
        view(atoms)

        pseudopotentials = {}

        for atom in atoms:
            pseudopotentials[atom.symbol] = atom.symbol + ".upf"

        print(pseudopotentials)
        fd = "qe.pwi"

        output = io.StringIO()

        write_espresso_in(output, atoms, input_data=input_data, pseudopotentials=pseudopotentials, kpts=(12, 12, 1),
                          koffset=(0, 0, 0))

        return output.getvalue()


if __name__ == '__main__':

    tool = PrintVASP2QE()
    tool.entry_point()
