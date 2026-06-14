import sys

def remove_self_closing_lines(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = [
        line for line in lines
        if "/>" not in line
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

    print(f"Done. Removed {len(lines) - len(cleaned_lines)} lines.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python remove_self_closing.py input.xml output.xml")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    remove_self_closing_lines(input_file, output_file)