import numpy as np
from qe_micro_tools.xml2dict import xml2dict
from qe_micro_tools.formats_and_units import units, format_schema


def get_cell_to_print(data_dict, format='qe'):
    coef = units[data_dict['@Units'].split()[0]]

    a1 = data_dict['output']['atomic_structure']['cell']['a1']
    a2 = data_dict['output']['atomic_structure']['cell']['a2']
    a3 = data_dict['output']['atomic_structure']['cell']['a3']

    cell = np.vstack((a1, a2, a3)) * coef

    cell_to_print = [format_schema[format]['cell']['header']]

    for item in cell:
        cell_to_print.append(np.array2string(item, formatter={'float_kind': lambda x: f"{x: .10f}"})[1:-1])

    cell_to_print.append(format_schema[format]['cell']['footer'])
    cell_to_print = "\n".join(cell_to_print)

    return cell_to_print


def get_coords_to_print(data_dict, format='qe'):
    coords_to_print = [format_schema[format]['coords']['header']]

    for item in data_dict['output']['atomic_structure']['atomic_positions']['atom']:
        # coords_to_print.append(item['@name'] + " " + " ".join(str(x * units['bohr']) for x in item['$']))

        data = np.array2string(np.array(item['$']) * units['bohr'], formatter={'float_kind': lambda x: f"{x: .10f}"})[1:-1]
        coords_to_print.append(item['@name'] + " " + data)

        # cell_to_print.append(np.array2string(item, formatter={'float_kind': lambda x: f"{x:.10f}"})[1:-1])

    coords_to_print.append(format_schema[format]['coords']['footer'])
    coords_to_print = "\n".join(coords_to_print)

    return coords_to_print


if __name__ == '__main__':
    file_name = '/Users/mykhailoklymenko/data-file-schema.xml'
    data_dict = xml2dict(file_name)

    cell = get_cell_to_print(data_dict)
    print(cell)
    coords = get_coords_to_print(data_dict)
    print(coords)
