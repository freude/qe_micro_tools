from abc import ABC, abstractmethod
import argparse


class Microtool(ABC):

    def __init__(self, **kwargs):
        self.description = kwargs.get("description", "No description provided")
        self.file_path = None
        self.parser = argparse.ArgumentParser(description=self.description)

        self.parser.add_argument(
            "file_name",
            metavar="XML_FILE",
            help="Path to the Quantum ESPRESSO XML file."
        )

        self.parser.add_argument("--save", action=argparse.BooleanOptionalAction)

    def entry_point(self):

        args = self.parser.parse_args()
        result = self.implementation(args)

        if args.save:
            file_path = "coords.out"
            try:
                # Open the file in 'w' (write) mode
                with open(file_path, 'w') as text_file:
                    text_file.write(result)
                print(f"Successfully wrote string to {file_path}")
            except IOError as e:
                print(f"Error writing to file: {e}")

    @abstractmethod
    def implementation(self, args):
        pass




