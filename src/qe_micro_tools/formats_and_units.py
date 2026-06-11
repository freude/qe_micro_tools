
units = {'Hartree': 0.52917721090380, 'bohr': 5.29177210903e-11 / 1e-10}

format_schema = {
    'qe': {'cell': {'header': 'CELL_PARAMETERS angstrom',
                    'footer': ''},
           'coords': {'header': 'ATOMIC_POSITIONS angstrom',
                      'footer': ''},
           },
    'wan': {'cell': {'header': 'begin unit_cell_cart\nAng',
                     'footer': 'end unit_cell_cart\n'},
            'coords': {'header': 'begin atoms_cart\nAng',
                       'footer': 'end atoms_cart\n'},
            }
}
