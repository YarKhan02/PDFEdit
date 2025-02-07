import argparse
import os
import fitz  # PyMuPDF
import sys

def remove_page(file_name, pages_to_remove, output_file):
    # Validate input file
    if not os.path.isfile(file_name):
        print("Error: Input file not found!")
        sys.exit(1)

    # Open file
    doc = fitz.open(file_name)

    # Remove pages 
    for i in pages_to_remove:
        try:
            doc.delete_page(i - 1)
        except Exception as e:
            print(f'Error removing page {i}: {e}')
            sys.exit(1)

    doc.save(output_file)
    print(f"Success! Saved as: {output_file}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <input.pdf> <pages_to_remove> [output_filename]")
        print("Example: python3 script.py file.pdf 1,2,3 external")
        sys.exit(1)

    file_name = sys.argv[1]
    try:
        pages_to_remove = list(map(int, sys.argv[2].split(",")))
        if any(p <= 0 for p in pages_to_remove):
            print("Error: Page numbers must be positive integers!")
            sys.exit(1)
    except ValueError:
        print("Error: Page numbers must be integers separated by commas! e.g -> (1,2,3)")
        sys.exit(1)

    if '.' in sys.argv[3]:
        print('Error: File should not contain extension')
        sys.exit(1)

    output_file = sys.argv[3] + '.pdf' if len(sys.argv) > 3 else "output.pdf"
    remove_page(file_name, pages_to_remove[::-1], output_file)