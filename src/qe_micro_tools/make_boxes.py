from qe_micro_tools.microtool_interface import Microtool
from qe_micro_tools.xml2dict import xml2dict



class PrintBoxes(Microtool):

    def __init__(self):

        description = ("Extract and print unit-cell lattice vectors"
                       "from a Quantum ESPRESSO XML output file.")

        super().__init__(description=description)

    def implementation(self, args):

        file_name = "all_projwfc.in"
        label = "ab_bilayer_scf"
        outdir = "tmp_" + label

        path = args.file_name
        a = xml2dict(path)
        fft_grid = list(a['output']['basis_set']['fft_grid'].values())
        # fft_grid = [36, 60, 270]
        num_of_boxes = fft_grid[2] // 2

        num_points1 = 0
        text_in = """n_proj_boxes = {}\n""".format(num_of_boxes)

        for j in range(num_of_boxes):
            num_points2 = int((j + 1) * fft_grid[2] / num_of_boxes) - 1

            text_in += """irmin(1,{}) = 0, irmax(1,{}) = {},
irmin(2,{}) = 0, irmax(2,{}) = {},
irmin(3,{}) = {}, irmax(3,{}) = {},""".format(j+1, j+1, fft_grid[0],
                                              j+1, j+1, fft_grid[1],
                                              j+1, num_points1, j+1, num_points2)

            text_in += "\n"
            num_points1 = num_points2

        print(text_in)
        return text_in


def main():
    tool = PrintBoxes()
    tool.entry_point()


if __name__ == "__main__":
    main()

